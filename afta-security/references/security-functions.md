# 2-6 Protection of product security functions

Original Persian text extracted from the supplied v1.9 document. Options are unselected and previous product answers are excluded. Source text defines the requirement; assessment guidance in workflow.md is supplied by this package.

## AFTA-2-6-01

محصول باید هنگام رخ دادن هرگونه خرابی، اشکال یا شکست مانند از کار افتادن محصول، قطع شدن ارتباط محصول با پایگاه داده و یا اختلال در کارکردهای محصول، در وضعیت امنی قرار گرفته، صحت داده‌ها و خط‌مشی کنترل دسترسی را حفظ نماید.

Source: table 7, row 1 (zero-based indices in the Word document XML).

### AFTA-2-6-01.s01

هر یکی از مواردی که در صورت رخداد آن، وضعیت امن محصول حفظ می‌شود، مشخص گردد.

خرابی‌های نرم‌افزاری

### AFTA-2-6-01.s02

خرابی‌های سخت‌افزاری

## AFTA-2-6-02

محصول باید از طریق فراهم نمودن بستر و زیرساخت امن، توانایی جلوگیری از افشاء یا تغییر داده، هنگام انتقال بین بخش‌های مجزای خود را داشته باشد.

Source: table 7, row 4 (zero-based indices in the Word document XML).

## AFTA-2-6-03

در صورتی که محصول از محصولات امن IT دیگری استفاده می‌کند، باید تفسیر سازگار و یکسانی را از داده امنیتی در زمان اشتراک‌گذاری آن بین خود و دیگر محصولات امن IT، فراهم آورد.

Source: table 7, row 5 (zero-based indices in the Word document XML).

Initial applicability: at least one of external_security_products. Unknown conditions do not establish non-applicability.

### AFTA-2-6-03.s01

داده امنیتی قابل اشتراک‌گذاری که در محصول پشتیبانی مـی‌شوند، مشخص گردد.

داده‌های احراز هویت

### AFTA-2-6-03.s02

کلید

### AFTA-2-6-03.s03

امضای دیجیتال

### AFTA-2-6-03.s04

ثبت‌نشان‌ها (داده‌های ممیزی)

### AFTA-2-6-03.s05

سایر موارد

## AFTA-2-6-04

محصول باید زمان و تاریخ معتبری داشته باشد، بنابراین باید مهرهای زمانی معتبر را تولید یا از آن‌ها استفاده نماید.

Source: table 7, row 11 (zero-based indices in the Word document XML).

### AFTA-2-6-04.s01

روش‌های ایجاد مهرهای زمانی معتبر انتخاب شود. (دیگـر روشهای موجـود در محصول، در قسـمت «سایر مـوارد» بیـان شود).

گرفتن مهرهای زمانی از سرور NTP

### AFTA-2-6-04.s02

تنظیم مهرهای زمانی از طریق اینترنت

### AFTA-2-6-04.s03

تنظیم مهرهای زمانی به صورت پیش‌فرض (معتبر و عدم امکان دستکاری غیرمجاز)

### AFTA-2-6-04.s04

سایر موارد

## AFTA-2-6-05

محصول باید امکان بروزرسانی نرم‌افزار و میان‌افزار محصول را برای مدیر سیستم فراهم نماید.

Source: table 7, row 16 (zero-based indices in the Word document XML).

### AFTA-2-6-05.s01

روش بروزرسانی مورد استفاده در محصول، مشخص گردد (حـداقل یک مورد لازم و کافی است).

بروزرسانی دستی

### AFTA-2-6-05.s02

جستجوی خودکار بروزرسانی‌ها

### AFTA-2-6-05.s03

بروزرسانی‌های خودکار

### AFTA-2-6-05.s04

بروزرسانی دستی بعد از اطمینان از امنیت وصله و یا فایل بروزرسانی

## AFTA-2-6-06

در صورت استفاده از بروزرسانی به روش خودکار، محصول باید پیش از نصب بروزرسانی‌های نرم‌افزاری و میان‌افزاری، امکان احراز اصالت میان‌افزار یا نرم‌افزار را فراهم نماید.

Source: table 7, row 21 (zero-based indices in the Word document XML).

Initial applicability: at least one of automatic_updates. Unknown conditions do not establish non-applicability.

### AFTA-2-6-06.s01

سازوکار مورد استفاده برای صحت‌سنجی (اصالت سنجی) به‌روزرسانی‌ها انتخاب گردد.

امضای دیجیتال

### AFTA-2-6-06.s02

درهم‌ساز منتشرشده
