# BeaconPilot Widget Installation Guide

## Quick Start

Add this single line of code to your website to integrate the BeaconPilot chat widget:

```html
<script src="https://yourdomain.com/widget-js/widget.js"></script>
```

Replace `yourdomain.com` with your actual domain where BeaconPilot is hosted.

## Features

- 💬 Clean, modern chat interface
- 🎯 Smart AI-powered responses
- 🎨 Customizable appearance
- 📱 Mobile-friendly design
- 🔒 Secure iframe implementation

## Development Setup

For local development, use:

```html
<script src="http://localhost:8000/widget-js/widget.js"></script>
```

## How It Works

1. The widget starts as a "Chat with us" button in the bottom right corner
2. Clicking the button opens the chat interface
3. The chat interface loads in a secure iframe
4. Messages are processed through your BeaconPilot backend
5. Responses are generated using AI and your FAQ data

## Technical Details

- Uses iframe for security and isolation
- Cross-origin communication handled securely
- Smooth animations and transitions
- Responsive design that works on all devices
- Minimal impact on page load performance

## Customization

The widget is designed to be easily customizable. You can modify:

- Colors
- Position
- Size
- Text
- Animations

To customize, edit the `widget.js` file in your BeaconPilot installation.

## Security

The widget uses several security features:

- Secure iframe isolation
- Origin verification for messages
- No external dependencies
- CORS protection
- XSS prevention

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Troubleshooting

1. Widget not loading?
   - Check your domain configuration
   - Verify CORS settings
   - Check browser console for errors

2. Chat not connecting?
   - Verify backend server is running
   - Check network connectivity
   - Verify API endpoints

3. Styling issues?
   - Check for CSS conflicts
   - Verify z-index settings
   - Check mobile viewport settings 