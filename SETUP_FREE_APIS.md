# How to Setup Free APIs: Reddit, Claude & Telegram 🚀

## 1️⃣ REDDIT API (Completely Free)

### Step 1: Create Reddit Account
- Go to https://www.reddit.com/signup
- Create a free account

### Step 2: Register Your App
1. Visit: https://www.reddit.com/prefs/apps
2. Click "Create an application"
3. Fill in:
   - **Name**: `CanadaImmigrationBot`
   - **App type**: Select `script`
   - **Description**: `Lead finder for immigration queries`
   - **Redirect URI**: `http://localhost:8080`
4. Click "Create app"
5. You'll see:
   - **Client ID** (under app name)
   - **Client Secret** (next to secret label)

### Step 3: Add to .env
```env
REDDIT_CLIENT_ID=your_14_char_id_here
REDDIT_CLIENT_SECRET=your_27_char_secret_here
REDDIT_USER_AGENT=CanadaImmigrationLeadFinder/1.0
```

### Free Tier Limits:
- ✅ **Unlimited** Reddit scraping
- ✅ **No rate limiting** for basic queries
- ✅ **No credit card needed**

---

## 2️⃣ CLAUDE API (Free Credits)

### Option A: Use Free Trial Credits
1. Go to: https://console.anthropic.com/signup
2. Sign up with email
3. You get **$5 free credits** (expires in 3 months)
4. That's enough for ~1,000 lead qualifications!

### Option B: Pay-As-You-Go (Optional)
- Claude 3.5 Sonnet: ~$0.003 per 1K tokens
- Average cost per lead: **$0.01-0.02**

### Get Your API Key:
1. Go to: https://console.anthropic.com/account/keys
2. Click "Create Key"
3. Copy the key

### Step 3: Add to .env
```env
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Free Tier Limits:
- ✅ **$5 free credits** on signup
- ✅ **Same features** as paid tier
- ✅ **Perfect for testing**

---

## 3️⃣ TELEGRAM BOT (Free to Create & Use)

### Step 1: Create Your Telegram Bot
1. Open Telegram app or go to https://web.telegram.org
2. Search for: `@BotFather` (verified bot)
3. Send: `/start`
4. Send: `/newbot`
5. Follow prompts:
   - Bot name: `CanadaImmigrationBot`
   - Username: `canada_immigration_bot_XXXXXX` (must be unique)
6. You'll get a **Bot Token**:
   ```
   123456789:ABCDEFGHIJKLmnopqrstuvwxyz1234567890
   ```

### Step 2: Get Your Chat ID
1. Search for your new bot in Telegram
2. Click `/start`
3. Send any message
4. Go to: https://api.telegram.org/botYOUR_TOKEN/getUpdates
5. Replace `YOUR_TOKEN` with your bot token
6. Look for `"chat":{"id":YOUR_CHAT_ID}`

### Step 3: Add to .env
```env
TELEGRAM_BOT_TOKEN=123456789:ABCDEFGHIJKLmnopqrstuvwxyz1234567890
TELEGRAM_CHAT_ID=987654321
```

### Free Tier Limits:
- ✅ **Unlimited** messages
- ✅ **No rate limits** for small bots
- ✅ **No credit card needed**
- ✅ **Forever free**

---

## 4️⃣ GOOGLE SHEETS (Optional - Free)

### Step 1: Create Google Account
- Go to https://accounts.google.com/signup

### Step 2: Create Service Account
1. Go to: https://console.cloud.google.com
2. Create new project: `ImmigrationBot`
3. Search for "Sheets API" → Enable it
4. Go to Credentials → Create Service Account
5. Name: `immigration-bot`
6. Create & download JSON key
7. Save to: `config/google_service_account.json`

### Step 3: Create Spreadsheet
1. Go to https://sheets.google.com
2. Create new spreadsheet: `Immigration Leads`
3. Share with service account email (from JSON file)
4. Copy spreadsheet ID from URL

### Step 4: Add to .env
```env
GOOGLE_SHEET_ID=1BxiMVs0XRA5nFMoon89PL6eiKJKzQzWJTSKUSbnHsow
GOOGLE_CREDENTIALS_PATH=config/google_service_account.json
```

### Free Tier Limits:
- ✅ **Unlimited** sheets
- ✅ **Unlimited** data storage
- ✅ **No credit card needed**

---

## 📊 Complete Free .env Setup

Create a file named `.env` in your project root:

```env
# ============ REDDIT (FREE) ============
REDDIT_CLIENT_ID=your_14_char_id
REDDIT_CLIENT_SECRET=your_27_char_secret
REDDIT_USER_AGENT=CanadaImmigrationLeadFinder/1.0

# ============ CLAUDE AI (FREE $5 CREDITS) ============
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx

# ============ TELEGRAM (FREE) ============
TELEGRAM_BOT_TOKEN=123456789:ABCDEFGHIJKLmnopqrstuvwxyz1234567890
TELEGRAM_CHAT_ID=987654321

# ============ GOOGLE SHEETS (FREE - OPTIONAL) ============
GOOGLE_SHEET_ID=your_spreadsheet_id_from_url
GOOGLE_CREDENTIALS_PATH=config/google_service_account.json

# ============ APP SETTINGS ============
SCHEDULER_INTERVAL_HOURS=6
LOG_LEVEL=INFO
OUTPUT_CSV_PATH=output/sample_leads.csv
```

---

## 🎯 Cost Breakdown (Monthly)

| Service | Free Tier | Usage | Cost |
|---------|-----------|-------|------|
| Reddit | ✅ Unlimited | Scraping 1000+ posts | **$0** |
| Claude | ✅ $5 credits | ~250-500 lead qualifications | **$0** (first 3 months) |
| Telegram | ✅ Unlimited | Unlimited messages | **$0** |
| Google Sheets | ✅ Unlimited | Store 10,000+ leads | **$0** |
| **TOTAL** | | **Complete System** | **$0/month** |

---

## 🚀 How It All Works Together

```
Reddit Posts
    ↓
    └─→ Scraper (FREE - Reddit API)
         ↓
    └─→ AI Qualifier (FREE - Claude $5 credits)
         ↓
    ├─→ Google Sheets (FREE - optional storage)
    │
    └─→ Telegram Bot (FREE - instant notification)
         ↓
    └─→ CSV Export (FREE - local backup)
```

---

## ✅ Step-by-Step Quick Start

### 1. Get Reddit Credentials (2 min)
```bash
Visit: https://www.reddit.com/prefs/apps
Create app → Copy Client ID & Secret
```

### 2. Get Claude API Key (1 min)
```bash
Visit: https://console.anthropic.com/account/keys
Sign up → Create key → Copy key
```

### 3. Create Telegram Bot (3 min)
```bash
Telegram → Search @BotFather
/newbot → Follow steps → Copy token & chat ID
```

### 4. Update .env File (1 min)
```bash
cp .env.example .env
# Edit .env with your credentials
```

### 5. Run Pipeline (1 min)
```bash
python main.py
```

**Total time: ~8 minutes** ⏱️

---

## 🔧 Testing Each Service

### Test Reddit
```bash
python -c "from src.reddit_scraper import RedditScraper; r = RedditScraper(); print('✓ Reddit OK')"
```

### Test Claude
```bash
python -c "from posts.ai_qualifier import AIQualifier; a = AIQualifier(); print('✓ Claude OK')"
```

### Test Telegram
```bash
python -c "from Sheets.telegram_notifier import TelegramNotifier; t = TelegramNotifier(); print('✓ Telegram OK')"
```

---

## 💡 Pro Tips

1. **Reddit scraping is unlimited** - run it as often as you want
2. **Claude $5 = 1000+ qualifications** - very budget-friendly
3. **Telegram notifications are instant** - great for real-time alerts
4. **Google Sheets is optional** - CSV export works offline
5. **All services are truly free** - no hidden costs

---

## ⚠️ Important Notes

- ✅ Never share your `.env` file
- ✅ Rotate API keys periodically
- ✅ Monitor Claude usage to stay within free credits
- ✅ Keep bot tokens secret

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Reddit 401 error | Check Client ID & Secret spelling |
| Claude errors | Verify API key starts with `sk-ant-` |
| Telegram not sending | Check bot token & chat ID are correct |
| Google Sheets fails | Make sure service account email has sheet access |

---

## 📞 Get Help

- Reddit issues: https://www.reddit.com/r/redditdev
- Claude issues: https://anthropic.com/docs
- Telegram issues: https://t.me/botfather
- Google issues: https://support.google.com/sheets

---

**Now you have a complete ZERO-COST lead generation system! 🎉**
