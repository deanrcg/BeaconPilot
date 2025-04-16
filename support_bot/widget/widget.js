(function() {
  // Get the current script tag to determine the base URL
  const script = document.currentScript;
  const baseUrl = new URL(script.src).origin;
  
  // Create chat button
  const button = document.createElement("button");
  button.innerHTML = "Chat with us";
  button.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    padding: 12px 24px;
    background: #d39d5c;
    color: white;
    border: none;
    border-radius: 25px;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
    cursor: pointer;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    z-index: 999999;
  `;
  
  // Create iframe
  const iframe = document.createElement("iframe");
  iframe.style.cssText = `
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 320px;
    height: 440px;
    border: none;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    z-index: 999999;
    transition: all 0.3s ease;
    opacity: 0;
    transform: translateY(20px);
    pointer-events: none;
  `;
  
  // Set iframe source
  iframe.src = `${baseUrl}/widget`;
  
  // Add elements to page
  document.body.appendChild(button);
  document.body.appendChild(iframe);
  
  // Toggle chat on button click
  let isOpen = false;
  button.addEventListener("click", () => {
    isOpen = !isOpen;
    iframe.style.opacity = isOpen ? "1" : "0";
    iframe.style.transform = isOpen ? "translateY(0)" : "translateY(20px)";
    iframe.style.pointerEvents = isOpen ? "auto" : "none";
    button.innerHTML = isOpen ? "Close chat" : "Chat with us";
    button.style.background = isOpen ? "#2d4239" : "#d39d5c";
  });
  
  // Handle messages from iframe
  window.addEventListener("message", (event) => {
    if (event.origin !== baseUrl) return;
    
    if (event.data.type === "resize") {
      iframe.style.height = event.data.height + "px";
    }
  });
})(); 