# نصب و استفاده از چک‌لیست امنیت افتا

نسخهٔ بسته: **1.1.0**؛ نسخهٔ سند پایه: **1.9**.

یک Skill مشترک برای **Claude Code، GitHub Copilot، Cursor و Codex**؛ شامل ۷۹ الزام اصلی و ۳۰۷ ردیف گزینه و توضیح. متن عمومی الزامات از پاسخ‌های محصول قبلی جدا شده است.

## نصب سریع برای همهٔ ابزارها

ZIP را دانلود و کامل استخراج کنید. ترمینال را در پوشه‌ای باز کنید که `install.sh`، `install.ps1` و پوشهٔ `afta-security` کنار هم قرار دارند. نصب کاملاً آفلاین است و به Git، Node، Python یا دسترسی مدیر سیستم نیاز ندارد.

### Bash در Linux و macOS و Git Bash

نصب برای تمام پروژه‌های کاربر فعلی:

```bash
bash ./install.sh --agent all --scope user
```

نصب در یک پروژه برای اشتراک با تیم؛ مسیر را عوض کنید:

```bash
bash ./install.sh --agent all --scope project --project "/path/to/project"
```

اگر ترمینال در خود پروژه باز است، مسیر کامل نصب‌کننده را بدهید:

```bash
bash "/path/to/extracted-package/install.sh" --agent all --scope project
```

### PowerShell در Windows

نصب برای تمام پروژه‌های کاربر فعلی با Windows PowerShell 5.1:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope user
```

نصب در یک پروژه برای اشتراک با تیم؛ مسیر را عوض کنید:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope project -Project "C:\work\my-project"
```

گزینهٔ ExecutionPolicy فقط روی همان فرایند نصب اثر می‌گذارد و سیاست دائمی سیستم را تغییر نمی‌دهد. محدودیت‌های سازمانی ممکن است همچنان اعمال شوند.

### PowerShell 7 در Windows، Linux و macOS

```powershell
pwsh -NoProfile -File ./install.ps1 -Agent all -Scope user
```

برای پروژه در PowerShell 7:

```powershell
pwsh -NoProfile -File ./install.ps1 -Agent all -Scope project -Project "/path/to/project"
```

در Windows برای Project از مسیر Windows استفاده کنید. پس از نصب یک نشست تازه در ابزار موردنظر باز کنید. برنامهٔ میزبان باید از Agent Skills پشتیبانی کند؛ برای Copilot از حالت Agent یا محیط‌های پشتیبان Skill استفاده کنید. نصب فایل‌ها به معنای نصب خود ابزارهای هوش مصنوعی نیست.

## نصب برای یک ابزار مشخص

به جای `all` یکی از نام‌های زیر را انتخاب کنید. مثال‌ها نصب شخصی‌اند؛ برای نصب تیمی Scope را project کنید.

| ابزار | Bash | پارامتر PowerShell |
|---|---|---|
| Claude Code | `bash ./install.sh --agent claude-code --scope user` | `-Agent claude-code -Scope user` |
| GitHub Copilot | `bash ./install.sh --agent copilot --scope user` | `-Agent copilot -Scope user` |
| Cursor | `bash ./install.sh --agent cursor --scope user` | `-Agent cursor -Scope user` |
| Codex | `bash ./install.sh --agent codex --scope user` | `-Agent codex -Scope user` |

یک فرمان کامل برای نصب اختصاصی Claude Code در Windows:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent claude-code -Scope user
```

## مسیرهای نصب

همهٔ مسیرهای زیر به پوشهٔ `afta-security` ختم می‌شوند. `~` پوشهٔ کاربر فعلی است؛ در Windows معمولاً همان UserProfile است.

| انتخاب | نصب شخصی | نصب در پروژه |
|---|---|---|
| `codex` | `~/.agents/skills/afta-security` | `.agents/skills/afta-security` |
| `claude-code` | `~/.claude/skills/afta-security` | `.claude/skills/afta-security` |
| `cursor` | `~/.cursor/skills/afta-security` | `.cursor/skills/afta-security` |
| `copilot` | `~/.copilot/skills/afta-security` | `.github/skills/afta-security` |

انتخاب `all` دو کپی یکسان در `.agents/skills` و `.claude/skills` می‌گذارد. مسیر مشترک agents توسط Codex، Cursor و Copilot خوانده می‌شود؛ مسیر claude برای Claude Code است. برای یک دامنهٔ نصب، یکی از روش‌های all یا نصب اختصاصی را انتخاب کنید؛ ترکیب آن‌ها ممکن است نسخه‌های تکراری قابل‌کشف ایجاد کند. بعضی ابزارها چند مسیر سازگار را می‌خوانند.

اگر قبلاً نسخهٔ 1.0.0 را در `~/.codex/skills/afta-security` نصب کرده‌اید، آن کپی قدیمی را پس از انتقال تغییرات شخصی خارج از پوشه‌های کشف Skill نگه دارید؛ نصب‌کننده مسیر قدیمی را پاک یا مهاجرت نمی‌کند. نصب هم‌زمان نسخه‌های شخصی و پروژه‌ای با نام یکسان نیز ممکن است انتخاب نسخه را مبهم کند.

در WSL، نصب Bash داخل محیط Linux انجام می‌شود؛ نصب شخصی Windows و WSL جداست. مسیر پروژه باید وجود داشته باشد. نصب پروژه‌ای فقط همان پوشه‌های Skill را اضافه می‌کند؛ آن‌ها را برای اشتراک با همکاران در مخزن پروژه ثبت کنید. نصب شخصی به‌صورت خودکار به محیط ابری یا دستگاه همکاران منتقل نمی‌شود.

## پیش‌نمایش و به‌روزرسانی

نمایش مسیرها بدون نوشتن فایل:

```bash
bash ./install.sh --agent all --scope project --project "/path/to/project" --dry-run
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope project -Project "C:\work\my-project" -DryRun
```

نصب مجدد نسخهٔ یکسان تغییری ایجاد نمی‌کند. اگر نسخهٔ موجود متفاوت باشد، نصب متوقف می‌شود. برای به‌روزرسانی آگاهانه، Force را اضافه کنید:

```bash
bash ./install.sh --agent all --scope user --force
```

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent all -Scope user -Force
```

نسخهٔ قبلی به پوشهٔ `.afta-security-backups` در ریشهٔ پروژه یا پوشهٔ کاربر منتقل می‌شود؛ این پوشه خارج از مسیر کشف Skill است. مسیر نسخهٔ پشتیبان در خروجی نمایش داده می‌شود. پوشه‌های دیگر مهارت‌ها تغییر نمی‌کنند. به‌روزرسانی هر مقصد جدا انجام می‌شود؛ اگر در میانهٔ نصب چندمقصدی خطا رخ دهد، مقصدهای تکمیل‌شده باقی می‌مانند و پس از رفع خطا می‌توانید فرمان را دوباره اجرا کنید.

برای حذف، فقط پوشه‌های `afta-security` مربوط به روش نصب انتخاب‌شده را بردارید. برای بازگرداندن نسخهٔ قبلی، نسخهٔ فعلی همان مقصد را از مسیر کشف خارج و پوشهٔ پشتیبان را به مسیر قبلی برگردانید.

## استفاده

در همهٔ ابزارها می‌توانید به زبان طبیعی بنویسید:

```text
از مهارت afta-security برای بررسی این پروژه بر اساس چک‌لیست افتا نسخهٔ ۱٫۹ استفاده کن.
برای هر بند شاهد، وضعیت، کمبود و اقدام بعدی بنویس.
مواردی که نیازمند آزمون محیط یا تفسیر مسئول امنیت هستند را نیازمند بررسی علامت بزن.
```

در Claude Code و Cursor، از `/afta-security` یا انتخاب Skill در منوی `/` استفاده کنید. در Codex، `$afta-security` را در درخواست بیاورید. در Copilot نام Skill را در درخواست Agent ذکر کنید؛ متن و منابع موردنیاز باید در محیط اجرای عامل در دسترس باشند.

برای پیاده‌سازی:

```text
از مهارت afta-security برای پیاده‌سازی ورود و مدیریت نشست طبق بندهای مرتبط استفاده کن.
شناسهٔ الزام، معیار پذیرش و نتیجهٔ آزمون را گزارش بده.
```

## گزارش ساختاریافته و Python اختیاری

خود چک‌لیست و تهیهٔ گزارش متنی به Python وابسته نیست. برای ابزار اختیاری JSON/Markdown به Python 3.9 یا جدیدتر نیاز دارید. فرمان `python3` در Linux/macOS و `py -3` یا `python` در Windows را مطابق نصب دستگاه انتخاب کنید.

`assets/project-profile.json` را از محل نصب Skill به پروژه کپی کنید، سپس نام، نسخه یا commit، محیط و دامنه را پر کنید. قابلیت‌های نامعلوم باید null بمانند؛ برای مقادیر true/false شاهد ثبت کنید. مثال در `references/workflow.md` است.

نمونهٔ Bash با نصب مشترک شخصی:

```bash
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" init --profile project-profile.json --out afta-report.json
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" validate afta-report.json
python3 "$HOME/.agents/skills/afta-security/scripts/afta.py" render afta-report.json --out afta-report.md
```

نمونهٔ Windows PowerShell با نصب مشترک شخصی:

```powershell
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" init --profile project-profile.json --out afta-report.json
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" validate afta-report.json
py -3 "$HOME/.agents/skills/afta-security/scripts/afta.py" render afta-report.json --out afta-report.md
```

برای نصب اختصاصی یا پروژه‌ای، مسیر اسکریپت را طبق جدول مسیرها عوض کنید. همهٔ بندها ابتدا «نیازمند بررسی» ثبت می‌شوند. ابزار اسکنر کد نیست؛ صحت و کفایت شواهد باید بررسی شود. اعتبارسنجی فقط ساختار و اطلاعات لازم را بررسی می‌کند. گزارش موجود بازنویسی نمی‌شود.

## نسخهٔ پایه و نگهداری

بانک مشترک الزامات `references/catalog.json` است. تغییر متن منبع، تفسیر شرکت و تصمیم پروژه را جدا نگه دارید. فایل Word اولیه توزیع نشده و اثر انگشت آن در بانک الزامات ثبت شده است. اصالت و آخرین‌بودن سند ارسالی مستقلاً تأیید نشده است. ابهام‌های TLS و گواهی‌نامه در `references/source-notes.md` ثبت شده‌اند؛ بررسی عامل جای تأیید رسمی را نمی‌گیرد.

مسیرهای نصب بر اساس مستندات رسمی بررسی شده‌اند:

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Cursor Agent Skills](https://prod.cursor.com/docs/skills)
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)

## بررسی نصب‌کننده‌ها

نصب برای همهٔ ابزارها و برای هر ابزار به‌تنهایی، مسیرهای دارای فاصله/حروف فارسی/براکت، پیش‌نمایش بدون نوشتن، نصب مجدد یکسان، رد بازنویسی بدون Force، حفظ نسخهٔ قبلی و برخورد با مقصد نامعتبر آزمایش شدند. Bash و PowerShell 7.7 روی Linux اجرا شدند؛ اجرای مستقیم روی Windows و Windows PowerShell 5.1 و همچنین اجرای واقعی عامل در هر چهار محصول آزمایش نشده است. نصب‌کنندهٔ PowerShell از قابلیت‌های سازگار با نسخهٔ 5.1 استفاده می‌کند. پشتیبانی مسیرها با مستندات رسمی تطبیق داده شده است.
