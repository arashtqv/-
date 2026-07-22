# -
# 🎮 Rock Paper Scissors Telegram Bot

A fun and interactive **Rock Paper Scissors Telegram Game Bot** built with Python and Telebot.

This bot allows users to play Rock Paper Scissors against the bot, manage their virtual budget, and try to increase their balance by winning games.

---

## 🚀 Features

✅ Interactive Telegram game  
✅ Rock / Paper / Scissors gameplay  
✅ Random bot choices  
✅ Virtual money system  
✅ Individual balance for each user  
✅ Win and lose reward system  
✅ User budget checking  
✅ Game continuation system (Yes / No)  
✅ Developer information section  
✅ Donation/support section  
✅ Inline keyboard buttons  
✅ Reply keyboard menu  

---

## 🎯 Game Rules

The game starts with:

```
💰 Starting Balance: 30,000 Toman
```

### Winning:
```
+10,000 Toman
```

### Losing:
```
-20,000 Toman
```

### Game limitations:

- If your balance goes below **10,000 Toman**, you cannot continue.
- If your balance reaches **100,000 Toman**, you win the game.

---

# 🖥️ Demo

Example:

```
User:
سنگ

Bot:
انتخاب شما: سنگ
انتخاب ربات: قیچی

Result:
You Win!

Your Balance:
40,000 Toman
```

---

# 🛠️ Technologies Used

## Programming Language

🐍 Python 3

## Libraries

- pyTelegramBotAPI (Telebot)
- python-dotenv
- random
- logging

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/telegram-rock-paper-scissors.git
```

Enter the project:

```bash
cd telegram-rock-paper-scissors
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create environment file

Create a file named:

```
.env
```

Add your Telegram Bot Token:

```env
API_TOKEN=YOUR_BOT_TOKEN
```

---

## 4. Run the bot

```bash
python main.py
```

---

# 📂 Project Structure

```
Telegram-RPS-Bot
│
├── main.py
├── .env
├── requirements.txt
├── README.md
│
└── assets
    └── screenshots
```

---

# 📋 Commands

| Command | Description |
|--------|-------------|
| /start | Start the bot |
| بودجه من | Show current balance |
| سازنده ی بازی | Show developer information |
| donate us | Support the project |

---

# 🎮 How To Play

1. Start the bot using:

```
/start
```

2. Press:

```
بزن بریم!
```

3. Choose:

```
سنگ
کاغذ
قیچی
```

4. After each round:

```
بله
```

Continue playing.

or

```
خیر
```

Stop the game.

---

# 🧠 Code Highlights

## User Balance System

Each user has a separate balance:

```python
budgets = {}
```

Example:

```python
budgets[user_id] = 30000
```

This prevents users from sharing the same balance.

---

## Random Bot Choice

The bot randomly selects:

```python
choices = [
    "سنگ",
    "کاغذ",
    "قیچی"
]
```

---

# 🔒 Environment Variables

Sensitive information such as Telegram API tokens is stored in `.env`.

Example:

```
API_TOKEN=xxxxxxxx
```

Never upload your `.env` file to GitHub.

---

# 🔮 Future Improvements

Planned features:

- [ ] SQLite database support
- [ ] Permanent user balances
- [ ] User ranking system
- [ ] Leaderboard
- [ ] Admin panel
- [ ] More games
- [ ] Payment system
- [ ] Better UI buttons
- [ ] Statistics dashboard

---

# 👨‍💻 Developer

Created by:

**Arash Taghavi**

Telegram:
```
@arash1390tqv
```

---

# ⭐ Support

If you like this project:

⭐ Star the repository

🐛 Report bugs

💡 Suggest new features

---

# 📜 License

This project is open source and available under the MIT License.
