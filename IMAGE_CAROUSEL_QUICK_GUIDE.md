# 🖼️ Image Carousel Quick Start Guide

## What's New?

Your index page (หน้าแรก) now displays images with an interactive carousel! Each place can have multiple images that you can scroll through.

## Features

### 📍 Index Page (หน้าแรก)

- **Arrow Buttons**: ◀️ ▶️ (visible when you hover over the image)
- **Image Counter**: Shows "1 / 5" (current image / total images)
- **Auto-Play**: Images change automatically every 4 seconds
- **Smooth Transitions**: Fade effect between images

### 📅 Place Detail Page

- Full image gallery with thumbnail previews
- Same arrow navigation
- Click thumbnails to jump to that image

## How to Use

### Uploading Multiple Images

When adding or editing a place:

1. Click "เลือกรูปภาพ" (Choose Images)
2. Select up to 10 images
3. The first image will be the thumbnail
4. Save - all images stored automatically

### Viewing Images

1. **Index Page**: Hover over place image to see arrows
2. Click arrows to scroll through images
3. Or wait and they'll auto-scroll
4. Watch the counter to see which image you're on

## Technical Info

### Database

- New table: `place_image` stores all images
- Each image linked to a place
- Supports unlimited images per place

### File Storage

- Images saved to: `static/uploads/`
- Files named by upload time (unique)
- Old images removed when editing

### Compatibility

- Works with existing places
- Old single-image places still show
- New images added to new table automatically

## Example

```
Place: เขาแหนม

Images: 1 / 5  ←  Current View  →
┌─────────────────┐
│                 │
│   [Image 1]     │  ← Showing image 1
│                 │
└─────────────────┘

Images: 2 / 5
┌─────────────────┐
│                 │
│   [Image 2]     │  ← After clicking →
│                 │
└─────────────────┘
```

## Settings

### Auto-Play Speed

- Change in `index.html` line: `data-interval="4000"`
- 4000 = 4 seconds (increase for slower)

### Max Images

- Default: 10 images per place
- Change in `app.py` line: `for file in files[:10]`

### Image Size

- Width: 100% (responsive)
- Height: 192px (h-48 in Tailwind)
- Maintains aspect ratio (object-cover)

## Troubleshooting

### Images Not Showing?

1. Check images uploaded correctly
2. Verify file in `static/uploads/` folder
3. Check browser console (F12) for errors

### Carousel Not Working?

1. Browser JavaScript enabled?
2. More than 1 image uploaded?
3. Check browser console for JavaScript errors

### Images Look Pixelated?

1. Upload high-resolution images
2. JPG or PNG format
3. Recommended: 1920x1440px or larger

## Browser Support

✅ Chrome, Firefox, Safari, Edge
✅ Mobile browsers (iOS Safari, Android Chrome)
✅ Tablets
✅ Touch and mouse input

---

**Version**: 1.0
**Last Updated**: February 3, 2026
**Status**: ✅ Active & Working
