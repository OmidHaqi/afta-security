# 3-2 TLS client

Original Persian text extracted from the supplied v1.9 document. Options are unselected and previous product answers are excluded. Source text defines the requirement; assessment guidance in workflow.md is supplied by this package.

## AFTA-3-2-01

محصول باید TLS 1.2 (RFC 5246) را پیاده‌سازی و دیگر نسخه‌های TLS و SSL را رد کند. همچنین محصول باید TLS را با پشتیبانی از مجموعه‌های رمز زیر پیاده‌سازی نماید.

Source: table 12, row 1 (zero-based indices in the Word document XML).

Initial applicability: at least one of tls, tls_client. Unknown conditions do not establish non-applicability.

### AFTA-3-2-01.s01

ﻣﺠﻤﻮﻋﻪ رﻣﺰ ﻣﻮرد اﺳﺘﻔﺎده و ﭘﻴﺎده‌ﺳﺎزی‌شده ﻣﺤﺼﻮل، اﻧﺘﺨﺎب ﮔﺮدد.

TLS_AES_256_GCM_SHA384
0x1302
مطابق با RFC 8446

### AFTA-3-2-01.s02

TLS_AES_128_GCM_SHA256
0x1301
مطابق با RFC 8446

### AFTA-3-2-01.s03

TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
0x009F
مطابق با RFC 5288

### AFTA-3-2-01.s04

TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
0x009E
مطابق با RFC 5288

### AFTA-3-2-01.s05

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
0xC02F
مطابق با RFC 5289

### AFTA-3-2-01.s06

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
0xC030
مطابق با RFC 5289

### AFTA-3-2-01.s07

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
0xC02C
مطابق با RFC 5289

### AFTA-3-2-01.s08

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
0xC02B
مطابق با RFC 5289

### AFTA-3-2-01.s09

TLS_RSA_WITH_AES_256_GCM_SHA384
0x009D
مطابق با RFC 5288

### AFTA-3-2-01.s10

TLS_RSA_WITH_AES_128_GCM_SHA256
0x009C
مطابق با RFC 5288

### AFTA-3-2-01.s11

TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384
0xC02E
مطابق با RFC 5288

### AFTA-3-2-01.s12

TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
0xC02D
مطابق با RFC 5289

### AFTA-3-2-01.s13

TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384
0xC032
مطابق با RFC 5289

### AFTA-3-2-01.s14

TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256
0xC031
مطابق با RFC 5289

### AFTA-3-2-01.s15

TLS_DH_RSA_WITH_AES_256_GCM_SHA384
0x00A1
مطابق با RFC 5288

### AFTA-3-2-01.s16

TLS_DH_RSA_WITH_AES_128_GCM_SHA256
0x00A0
مطابق با RFC 5288

## AFTA-3-2-02

محصول باید مطابقت شناسه ارائه‌شده با شناسه مرجع را با توجه به بخش 6 از RFC 6125، تأیید نماید.

Source: table 12, row 18 (zero-based indices in the Word document XML).

Initial applicability: at least one of tls, tls_client. Unknown conditions do not establish non-applicability.

## AFTA-3-2-03

محصول باید کانال امن را فقط در صورت معتبر بودن گواهی‌نامه سرور برقرار سازد؛ بنابراین اگر گواهی‌نامه سرور غیرمعتبر به نظر رسید، محصول باید بر اساس موارد زیر رفتار نماید.

Source: table 12, row 19 (zero-based indices in the Word document XML).

Initial applicability: at least one of tls, tls_client. Unknown conditions do not establish non-applicability.

### AFTA-3-2-03.s01

در صورت پشتیبانی از اقدامات دیگر، در «سایر موارد» بیان گردد.

ارتباط را برقرار نکند

### AFTA-3-2-03.s02

برای برقراری ارتباط درخواست مجوز کند

### AFTA-3-2-03.s03

سایر موارد

## AFTA-3-2-04

محصول باید در پیام ClientHello برای استفاده از خم‌های بیضوی، بر اساس موارد زیر عمل نماید.

Source: table 12, row 23 (zero-based indices in the Word document XML).

Initial applicability: at least one of tls, tls_client. Unknown conditions do not establish non-applicability.

### AFTA-3-2-04.s01

در صورتی که محصول از خم‌های بیضوی استفاده می‌نماید، نوع خم باید مشخص گردد.

Supported Elliptic Curves Extension را ارائه نکند.

### AFTA-3-2-04.s02

Supported Elliptic Curves Extension را به همراه NIST Curveهای secp256r1 یا secp384r1 یا secp521r1 ارائه نماید.
