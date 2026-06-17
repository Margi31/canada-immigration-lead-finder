# Reddit API Setup - Complete Visual Guide 🔴

## ⚠️ Important: You Need a Reddit Account First

If you don't have one, create it here:
https://www.reddit.com/signup

---

## Method 1: Web Browser (Easiest)

### Step 1: Sign In to Reddit
```
1. Go to https://www.reddit.com/
2. Sign in with your account (top right corner)
3. Verify you're logged in (you should see your username)
```

### Step 2: Go to App Preferences
```
1. Click your profile icon (top right)
2. Select "User settings" (NOT preferences)
3. Click the "Apps" tab (left sidebar)
4. At the bottom, click "Developed applications"

Alternative direct link:
https://www.reddit.com/prefs/apps
```

**⚠️ If you get "Page Not Found", scroll down and check for:**
- "authorized applications" section
- "developed applications" section
- Or go directly to: https://www.reddit.com/prefs/apps

### Step 3: Create New Application
```
If you see "Preferences" page with empty app list:

LOOK FOR: "Create another app..." or "Create an app..." button
- Should be at the BOTTOM of the page
- Or there might be a heading "developed applications" with a button below it

Click that button!
```

**If the button is hard to find:**
- Try scrolling to the very bottom of the page
- Look for any button with text like:
  - "Create an app"
  - "Create application"
  - "Create new app"
  - "Add new application"

### Step 4: Fill Out the Form

You'll see a form with these fields:

```
┌─────────────────────────────────────────┐
│         Create an app form              │
├─────────────────────────────────────────┤
│                                         │
│ App name:        [Enter app name]       │
│                                         │
│ App type:        ◉ script               │
│                  ○ web app              │
│                  ○ installed app        │
│                                         │
│ Description:     [Enter description]    │
│                                         │
│ Redirect URI:    [http://localhost:8080]│
│                                         │
│ [ Create app ]   [ Cancel ]             │
│                                         │
└─────────────────────────────────────────┘
```

**Fill it like this:**

| Field | Value |
|-------|-------|
| **App name** | `CanadaImmigrationBot` |
| **App type** | SELECT: `script` (radio button) |
| **Description** | `Lead finder for immigration queries` |
| **About URL** | (leave blank) |
| **Redirect URI** | `http://localhost:8080` |

**IMPORTANT:**
- ✅ Select "script" (not web app)
- ✅ Use exactly: `http://localhost:8080` for redirect URI
- ✅ Don't use `https://`, use `http://`

### Step 5: Click "Create app"

After clicking, you'll see your new app listed!

---

## Step 6: Get Your Credentials

**You'll see something like this:**

```
┌─────────────────────────────────────────────────────┐
│  CanadaImmigrationBot (script)                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Client ID:                                         │
│  ┌─────────────────────────────────────────────┐  │
│  │ a1b2c3d4e5f6g7h                             │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  Secret:                                            │
│  ┌─────────────────────────────────────────────┐  │
│  │ ••••••••••••••••••••••••••••••••••••••••••  │  │
│  └─────────────────────────────────────────────┘  │
│  (Click "show" to reveal secret)                   │
│                                                     │
│  Redirect URI:  http://localhost:8080              │
│  Created:       2024-01-15                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### What You Need to Copy:

1. **Client ID** (the visible string, looks like: `a1b2c3d4e5f6g7h`)
   - 14 characters usually
   - Copy exactly as shown

2. **Client Secret** (click "show" first to reveal)
   - 27 characters usually
   - Looks like random letters and characters
   - Click the eye icon or "show" button to see it
   - Copy exactly as shown

---

## Troubleshooting: "I Can't Find the App Creation Button"

### If you see a BLANK APP LIST:

```
Preferences
├── Apps
│   └── (empty area)
│       └── Look here: Is there a button at the bottom?
```

**Solution 1: Scroll Down**
- Press `End` key to go to bottom of page
- Look for "Create app" button

**Solution 2: Check If You're In Right Place**
```
You should be at: https://www.reddit.com/prefs/apps
- Check URL bar matches exactly
- If not, copy-paste that URL
```

**Solution 3: Check Browser Tab**
- Make sure you're on "Apps" tab (not "Authorized")
- Click "Apps" tab first

**Solution 4: Try This Direct URL**
Copy-paste exactly:
```
https://www.reddit.com/prefs/apps
```

---

## Troubleshooting: "I Don't See Any Apps Listed"

### Option 1: Clear Browser Cache
```
1. Press Ctrl+Shift+Delete
2. Click "Clear browsing data"
3. Select "All time"
4. Reload the page
```

### Option 2: Try Different Browser
```
- Chrome
- Firefox
- Edge
- Safari
- Opera
```

### Option 3: Try Reddit Mobile App
```
1. Download Reddit app
2. Log in
3. Go to Settings → Apps
4. Create app there
```

---

## Troubleshooting: Can't Find "Create App" Button

The button might be:
- ⬇️ At the **bottom** of the page (scroll down!)
- 📍 Under a heading like "developed applications"
- 🔘 In a dropdown menu (look for "Create" dropdown)
- ➕ As a "+" icon or plus button

**Try these searches:**
- `Ctrl+F` on Windows (or `Cmd+F` on Mac)
- Type: `create`
- Look for highlighted button

---

## Troubleshooting: "Invalid Application Type"

Make sure you select:
```
◉ script    ← SELECT THIS ONE
○ web app
○ installed app
```

NOT "web app" or "installed app" - must be **script**

---

## Alternative: Use Reddit App (Mobile)

If web browser isn't working:

```
1. Download Reddit app
2. Open Settings (gear icon)
3. Scroll to "Apps"
4. Tap "Create app"
5. Follow same steps as web browser
6. Copy credentials
```

---

## Step 7: Copy to .env File

Once you have your credentials:

**NEVER commit or share these!**

Create `.env` file in project root:

```env
REDDIT_CLIENT_ID=a1b2c3d4e5f6g7h
REDDIT_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
REDDIT_USER_AGENT=CanadaImmigrationLeadFinder/1.0
```

---

## How to Copy Without Mistakes

### The RIGHT Way (Recommended):
```
1. Click on Client ID field
2. Use Ctrl+A to select all
3. Use Ctrl+C to copy
4. Paste in .env file with Ctrl+V
5. Do NOT manually type it (mistakes happen!)
```

### Verify It's Right:
- Client ID length: 10-20 characters
- Client Secret length: 25-35 characters
- No spaces at beginning or end
- Check for typos by comparing

---

## Test Your Credentials

Run this command to verify they work:

```bash
python test_apis.py
```

You should see:
```
✅ Reddit API connection: SUCCESS
```

If you see error:
```
❌ Reddit API connection: FAILED
Error: received 401 HTTP response
```

This means credentials are wrong. Go back and re-copy.

---

## Common Mistakes & Fixes

| Mistake | How to Fix |
|---------|-----------|
| Wrong app type (web app instead of script) | Create a new app, select "script" |
| Copied with extra spaces | Use Ctrl+A then Ctrl+C, paste fresh |
| Wrong redirect URI | Use exactly: `http://localhost:8080` |
| Credentials expired | Create new credentials |
| Case sensitivity | Reddit credentials are case-sensitive, copy exactly |
| Used HTTPS instead of HTTP | Use `http://` not `https://` in redirect |

---

## Quick Reference Card

```
✓ Account needed? YES (free signup)
✓ What type? script
✓ Redirect URI? http://localhost:8080
✓ Cost? $0 forever
✓ Rate limit? None for basic use
✓ Approval needed? No, instant
```

---

## Still Having Issues?

### Debug Steps:

1. **Are you logged in?**
   - Check if you see your username in top right
   - If not, log in first

2. **Are you on the right page?**
   - URL should be: https://www.reddit.com/prefs/apps
   - Paste this in URL bar to be sure

3. **Is your account old enough?**
   - Reddit requires account to be 3 days old
   - If brand new account, wait 3 days

4. **Are you on the "Apps" tab?**
   - Click the "Apps" tab (not Authorized applications)

5. **Try Firefox?**
   - Sometimes Chrome has caching issues
   - Firefox works more reliably for this

---

## Video Alternative

If text is confusing, search YouTube for:
```
"reddit create app 2024"
"reddit script credentials"
"reddit app registration"
```

Look for videos from 2024 (most recent)

---

## Need Help?

If still stuck:

1. **Screenshot the page you're on**
2. **Check r/redditdev subreddit**
3. **Try Reddit API documentation**
   - https://www.reddit.com/dev/api/

---

## Success! ✅

When you see your app listed with:
- ✅ Client ID (14 chars)
- ✅ Client Secret (27+ chars)
- ✅ Redirect URI set

You're done! Copy these to .env file and you're ready to go!

---

**Problem resolved? Run this:**
```bash
python test_apis.py
```

Should see: `✅ Reddit API connection: SUCCESS`
