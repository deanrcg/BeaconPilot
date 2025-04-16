from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from typing import List, Optional
from pathlib import Path
from jose import JWTError, jwt

from .auth import (
    authenticate_user,
    create_access_token,
    fake_users_db,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    Token,
    User,
    TokenData,
    get_user,
    SECRET_KEY,
    ALGORITHM
)

# Get the directory containing routes.py
current_dir = Path(__file__).parent

router = APIRouter()
templates = Jinja2Templates(directory=str(current_dir / "templates"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/token", auto_error=False)

async def get_current_user(request: Request, token: Optional[str] = Depends(oauth2_scheme)):
    if not token:
        return RedirectResponse(url="/admin/login")
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@router.get("/admin/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.post("/admin/token")
async def login_for_access_token(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    user = authenticate_user(fake_users_db, username, password)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Incorrect username or password"
            },
            status_code=401
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    response = RedirectResponse(url="/admin/", status_code=302)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True
    )
    return response

@router.get("/admin/", response_class=HTMLResponse)
async def admin_dashboard(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": current_user,
            "stats": {
                "total_users": 100,  # Replace with actual stats
                "active_chats": 25,
                "revenue": "$1,234.56"
            }
        }
    )

@router.get("/admin/users", response_class=HTMLResponse)
async def admin_users(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "users.html",
        {
            "request": request,
            "user": current_user,
            "users": []  # Replace with actual user list
        }
    )

@router.get("/admin/settings", response_class=HTMLResponse)
async def admin_settings(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "settings.html",
        {
            "request": request,
            "user": current_user
        }
    )

@router.get("/admin/logout")
async def logout():
    response = RedirectResponse(url="/admin/login")
    response.delete_cookie("access_token")
    return response 