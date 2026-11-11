# 2-2 Cryptography

Original Persian text extracted from the supplied v1.9 document. Options are unselected and previous product answers are excluded. Source text defines the requirement; assessment guidance in workflow.md is supplied by this package.

## AFTA-2-2-01

محصول باید قابلیت رمزنگاری یا واحد رمزنگاری داشته باشد، بنابراین باید رمزگذاری و رمزگشایی را بر اساس الگوریتم AES (تعریف‌شده ISO 18033-3) با توجه به موارد زیر انجام دهد.

Source: table 3, row 1 (zero-based indices in the Word document XML).

### AFTA-2-2-01.s01

مد عملیاتی که الگوریتم از آن استفاده می‌کند را انتخاب نمایید. (وجود یک مورد لازم و کافی است.)

مد عملیاتی CBC و طول کلید 128 یا 192 یا 256 بیتی (تعریف‌شده در NIST SP 800-38A)

### AFTA-2-2-01.s02

مد عملیاتی GCM و طول کلید 128 یا 192 یا 256 بیتی (تعریف‌شده در NIST SP 800-38D)

### AFTA-2-2-01.s03

مد عملیاتی CTR و طول کلید 128 یا 192 یا 256 بیتی (تعریف‌شده در ISO10116)

## AFTA-2-2-02

محصول باید بر اساس الگوریتم رمزنگاری و طول کلیدی که انتخاب می‌نماید، توانایی تولید داده درهم‌سازی شده (Hash) را داشته باشد؛ بنابراین باید برای تولید درهم‌سازی از موارد زیر بر اساس ISO/IEC 10118-3:2004 استفاده نماید.

Source: table 3, row 5 (zero-based indices in the Word document XML).

### AFTA-2-2-02.s01

الگوریتم و اندازه خلاصه پیام مورد استفاده را انتخاب نمایید. (وجود یک مورد لازم و کافی است.)

الگوریتم SHA-1 با اندازه خلاصه پیام 160 بیت

### AFTA-2-2-02.s02

الگوریتم SHA-256 با اندازه خلاصه پیام 256 بیت

### AFTA-2-2-02.s03

الگوریتم SHA-384 با اندازه خلاصه پیام 384 بیت

### AFTA-2-2-02.s04

الگوریتم SHA-512 با اندازه خلاصه پیام 512 بیت

## AFTA-2-2-03

در صورتی که تولید کلید رمزنگاری در محصول وجود دارد، نیاز است که تخریب کلید رمزنگاری نیز بر اساس موارد زیر صورت پذیرد. (اختیاری)

Source: table 3, row 10 (zero-based indices in the Word document XML).

Initial applicability: at least one of key_generation. Unknown conditions do not establish non-applicability.

### AFTA-2-2-03.s01

روش نابودی کلید مشخص گردد. (وجود یک مورد لازم و کافی است)

نابودی با استفاده از بازنویسی ساده (بازنویسی با صفرها، یک‌ها، مقدار تصادفی، مقدار جدیدی از کلید)

### AFTA-2-2-03.s02

نابودی با استفاده از یک واسط مشخص

### AFTA-2-2-03.s03

از طریق توابع امنیتی محصول

### AFTA-2-2-03.s04

سایر موارد

## AFTA-2-2-04

در صورتی که امضای دیجیتال در محصول پشتیبانی می‌شود، نیاز است که سرویس‌های امضای رمزنگاری (تولید و تأیید) بر اساس الگوریتم‌های رمزنگاری زیر انجام گیرد. (اختیاری)

Source: table 3, row 15 (zero-based indices in the Word document XML).

Initial applicability: at least one of digital_signatures. Unknown conditions do not establish non-applicability.

### AFTA-2-2-04.s01

الگوریتم و اندازه کلیدهای مورد استفاده را انتخاب نمایید. (وجود یک مورد لازم و کافی است)

الگوریتم‌های امضای دیجیتال RSA با کلیدهای رمزنگاری 2048 بیت و بزرگتر
(بر اساس FIPS PUB 186-4، استاندارد امضای دیجیتال (DSS) بخش 5.5، الگوی امضای RSASSA-PSS نسخه PKCS #1 v2.1 و/یا RSASSA-PKCS1v_5؛ ISO/IEC 9796-2، الگوی امضای دیجیتال 2 و یا الگوی امضای دیجیتال 3)

### AFTA-2-2-04.s02

الگوریتم‌های امضای دیجیتال ECDSA با کلیدهای رمزنگاری 256 بیت یا بزرگتر
(بر اساس ISO/IEC 14888-3 بخش 6.4، استاندارد امضای دیجیتال (DSS) بخش 6 و پیوست D، با استفاده از منحنی P-256 یا P-384 یا P-521)
