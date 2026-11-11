# 3-5 Certificate validation

Original Persian text extracted from the supplied v1.9 document. Options are unselected and previous product answers are excluded. Source text defines the requirement; assessment guidance in workflow.md is supplied by this package.

## AFTA-3-5-01

محصول باید گواهی‌نامه‌ها را بر اساس قوانین زیر تأیید کند.

Source: table 15, row 1 (zero-based indices in the Word document XML).

Initial applicability: at least one of https, tls, tls_client, tls_server, certificate_validation. Unknown conditions do not establish non-applicability.

### AFTA-3-5-01.s01

تأیید گواهی‌نامه RFC 5280 و تأیید مسیر گواهی‌نامه که از حداقل طول مسیر دو گواهی‌نامه پشتیبانی می‌کند.

### AFTA-3-5-01.s02

مسیر گواهی‌نامه باید با یک گواهی‌نامه CA امن پایان یابد.

### AFTA-3-5-01.s03

محصول باید برای تأیید مسیر یک گواهی‌نامه، اطمینان حاصل نماید که افزونه basicConstraints وجود دارد و پرچم CA برای تمام گواهی‌نامه‌های CA به حالت «TRUE» تنظیم شده است.

### AFTA-3-5-01.s04

روش‌های تأیید وضعیت فسخ گواهی‌نامه

پروتکل وضعیت گواهی‌نامه آنلاین (OCSP) مشخص‌شده در RFC 696

### AFTA-3-5-01.s05

لیست فسخ گواهی‌نامه (CRL) مشخص شده در RFC 5280 بخش 6.3

### AFTA-3-5-01.s06

لیست فسخ گواهی‌نامه (CRL) مشخص شده در RFC 5759 بخش 5

### AFTA-3-5-01.s07

هیچ روش فسخ دیگری

### AFTA-3-5-01.s08

قوانین تأیید بخش extendedKeyUsage

گواهی‌نامه‌های مورد استفاده برای تأیید بروزرسانی‌های امن و اعتبارسنجی صحت کدهای اجرایی باید هدف «Code Signing» (id-kp3 با OID 1.3.6.1.5.5.7.3.1) را در بخش extendedKeyUsage خود داشته باشند.

### AFTA-3-5-01.s09

گواهی‌نامه‌های سرور ارائه شده برای TLS باید هدف «Server Authentication» (id-kp1 با OID 1.3.6.1.5.5.7.3.1) را در بخش extendedKeyUsage خود داشته باشند.

### AFTA-3-5-01.s10

گواهی‌نامه‌های کلاینت ارائه شده برای TLS باید هدف «Client Authentication» (id-kp1 با OID 1.3.6.1.5.5.7.3.2)  را در بخش extendedKeyUsage خود داشته باشند.

### AFTA-3-5-01.s11

گواهی‌نامه‌های OCSP مورد استفاده برای پاسخ OCSP باید «OCSP Signing» (id-pk9 با OID 1.3.6.1.5.5.7.3.9) را در بخش extendedKeyUsage خود داشته باشند.

## AFTA-3-5-02

محصول باید تنها در صورتی که افزونه مربوط به basicConstraints از پیش تنظیم شده باشد و همچنین، پرچم CA به حالت «TRUE» تنظیم شده باشد، یک گواهی‌نامه را به عنوان گواهی‌نامه CA بپذیرد.

Source: table 15, row 13 (zero-based indices in the Word document XML).

Initial applicability: at least one of https, tls, tls_client, tls_server, certificate_validation. Unknown conditions do not establish non-applicability.

## AFTA-3-5-03

محصول باید برای پشتیبانی از احراز هویت برای موارد زیر، از گواهی‌نامه‌های X509v3 تعریف‌شده در RFC 5280 استفاده کند.

Source: table 15, row 14 (zero-based indices in the Word document XML).

Initial applicability: at least one of https, tls, tls_client, tls_server, certificate_validation. Unknown conditions do not establish non-applicability.

### AFTA-3-5-03.s01

در صورت پشتیبانی از کارکردهای دیگر، در «سایر موارد» بیان گردد.

HTTPS

### AFTA-3-5-03.s02

TLS

### AFTA-3-5-03.s03

SSH

### AFTA-3-5-03.s04

امضای کد برای بروزرسانی‌های نرم‌افزار سیستم

### AFTA-3-5-03.s05

امضای کد برای تأیید یکپارچگی

### AFTA-3-5-03.s06

سایر موارد
