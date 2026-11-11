# 3-6 SSH

Original Persian text extracted from the supplied v1.9 document. Options are unselected and previous product answers are excluded. Source text defines the requirement; assessment guidance in workflow.md is supplied by this package.

## AFTA-3-6-01

محصول باید پروتکل SSH را مطابق با RFCهای 4251، 4252، 4253، 4254، 5656 و 6668 پیاده‌سازی نماید.

Source: table 16, row 1 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

## AFTA-3-6-02

محصول باید در پیاده‌سازی پروتکل SSH مطابق RFC 4252، از روش‌های احراز هویت زیر پشتیبانی نماید.

Source: table 16, row 2 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

### AFTA-3-6-02.s01

احراز هویت مبتنی بر کلید عمومی

### AFTA-3-6-02.s02

احراز هویت مبتنی بر گذرواژه

## AFTA-3-6-03

محصول باید در پیاده‌سازی پروتکل SSH مطابق RFC 4253، بسته‌های بزرگتر از مقدار مشخصی (در بخش «توضیحات» ذکر شود) را کنار بگذارد.

Source: table 16, row 5 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

## AFTA-3-6-04

محصول باید در پیاده‌سازی پروتکل SSH تنها از الگوریتم‌های رمزنگاری زیر استفاده نماید.

Source: table 16, row 6 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

### AFTA-3-6-04.s01

AES128-CBC

### AFTA-3-6-04.s02

AES192-CBC

### AFTA-3-6-04.s03

AES256-CBC

### AFTA-3-6-04.s04

AES128-CTR

### AFTA-3-6-04.s05

AES192-CTR

### AFTA-3-6-04.s06

AES256-CTR

### AFTA-3-6-04.s07

AEAD_AES_128_GCM

### AFTA-3-6-04.s08

AEAD_AES_256_GCM

## AFTA-3-6-05

محصول باید در پیاده‌سازی پروتکل انتقال SSH تنها از الگوریتم‌های کلید عمومی زیر استفاده نماید.

Source: table 16, row 15 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

### AFTA-3-6-05.s01

ssh-ed25519

### AFTA-3-6-05.s02

ssh-ed448

### AFTA-3-6-05.s03

rsa-sha2-512

### AFTA-3-6-05.s04

rsa-sha2-256

### AFTA-3-6-05.s05

ecdsa-sha2-nistp521

### AFTA-3-6-05.s06

ecdsa-sha2-nistp384

### AFTA-3-6-05.s07

ecdsa-sha2-nistp256

### AFTA-3-6-05.s08

x509v3-ecdsa-sha2-nistp521

### AFTA-3-6-05.s09

x509v3-ecdsa-sha2-nistp384

### AFTA-3-6-05.s10

x509v3-ecdsa-sha2-nistp256

### AFTA-3-6-05.s11

x509v3-rsa2048-sha256

### AFTA-3-6-05.s12

ssh-rsa

### AFTA-3-6-05.s13

x509v3-ssh-rsa

## AFTA-3-6-06

محصول باید در پیاده‌سازی پروتکل انتقال SSH تنها از الگوریتم‌های MAC صحت داده‌های زیر استفاده نماید.

Source: table 16, row 29 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

### AFTA-3-6-06.s01

AEAD_AES_256_GCM

### AFTA-3-6-06.s02

AEAD_AES_128_GCM

### AFTA-3-6-06.s03

hmac-sha2-512

### AFTA-3-6-06.s04

hmac-sha2-256

### AFTA-3-6-06.s05

hmac-sha1-96

### AFTA-3-6-06.s06

hmac-sha1

## AFTA-3-6-07

محصول باید در پیاده‌سازی پروتکل SSH تنها از الگوریتم‌های تبادل کلید زیر استفاده نماید.

Source: table 16, row 36 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

### AFTA-3-6-07.s01

curve25519-sha256

### AFTA-3-6-07.s02

curve448-sha512

### AFTA-3-6-07.s03

diffie-hellman-group-exchange-sha256

### AFTA-3-6-07.s04

diffie-hellman-group18-sha512

### AFTA-3-6-07.s05

diffie-hellman-group17-sha512

### AFTA-3-6-07.s06

diffie-hellman-group16-sha512

### AFTA-3-6-07.s07

diffie-hellman-group15-sha512

### AFTA-3-6-07.s08

ecdh-sha2-nistp521

### AFTA-3-6-07.s09

ecdh-sha2-nistp384

### AFTA-3-6-07.s10

ecdh-sha2-nistp256

### AFTA-3-6-07.s11

rsa2048-sha256

### AFTA-3-6-07.s12

diffie-hellman-group-exchange-sha1

### AFTA-3-6-07.s13

diffie-hellman-group14-sha256

## AFTA-3-6-08

محصول باید اطمینان پیدا کند که در یک ارتباط SSH، کلیدهای نشست یکسانی برای حد آستانه (طول نشست بیشتر از یک ساعت و حجم داده مبادله شده بیشتر از 1 گیگابایت نباشد) استفاده گردد. در صورت پر شدن حد آستانه برای هر کدام از موارد ذکر شده، باید تجدید کلید صورت بگیرد.

Source: table 16, row 50 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.

## AFTA-3-6-09

محصول باید اطمینان حاصل نماید که کلاینت SSH، سرور SSH را احراز هویت می‌کند. سرور SSH از یک پایگاه داده محلی که نام هر میزبان را با کلید عمومی متناظر آن (تشریح‌شده در RFC 4251 بخش ۷.1) همراه می‌کند، استفاده می‌نماید.

Source: table 16, row 51 (zero-based indices in the Word document XML).

Initial applicability: at least one of ssh. Unknown conditions do not establish non-applicability.
