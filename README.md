# MergeMKV
MergeMKV is a simple and powerful tool for merging single or multiple video and audio files. This Python script uses the FFMPEG tool to automatically combine audio (MP3) and video (MP4 or MKV) files that have the same name. Outputs are saved in MKV format and all operations are performed automatically with progress display.

[توضیح مستندات](#توضیح-مستندات)
[Documentation Explanation](#documentation-explanation)

---
## Table of Contents
1. [Project Introduction](#project-introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [File Structure](#file-structure)
5. [Usage](#usage)
6. [Possible Improvements](#possible-improvements)
7. [License](#license)

---
## فهرست مطالب
1. [مستندات](#توضیح-مستندات)
2. [ویژگی‌ها](#ویژگیها)
3. [پیش‌نیازها](#پیشنیازها)
4. [ساختار فایل‌ها](#ساختار-فایل‌ها)
5. [نحوه استفاده](#نحوه-استفاده)
6. [موارد قابل بهبود](#موارد-قابل-بهبود)
7. [لایسنس](#لایسنس)

### توضیح مستندات 

---

## **MergeMKV: ابزار ترکیب فایل‌های ویدیویی و صوتی با استفاده از FFMPEG**

اسکریپت `MergeMKV` یک اسکریپت پایتون است که به شما اجازه می‌دهد فایل‌های صوتی و ویدیویی مرتبط را به‌طور خودکار ادغام کرده و فایل‌های خروجی با فرمت MKV ایجاد کنید. این ابزار به صورت خاص برای محیط‌هایی طراحی شده که فایل‌های صوتی (مثلاً MP3) جداگانه از فایل‌های ویدیویی ذخیره شده‌اند و نیاز به ادغام آن‌ها وجود دارد.

---

### **ویژگی‌ها**

- **ادغام خودکار:** فایل‌های ویدیویی و صوتی که نام مشابه دارند را پیدا کرده و ترکیب می‌کند.
- **پشتیبانی از فرمت‌ها:** به‌طور پیش‌فرض از فرمت‌های ویدیویی `.mp4` و `.mkv` و فایل‌های صوتی `.mp3` پشتیبانی می‌کند.
- **پیش‌نیازهای حداقلی:** فقط نیاز به نصب پایتون و ابزار FFMPEG دارد.
- **نمایش نوار پیشرفت:** با استفاده از `tqdm`، پیشرفت پردازش فایل‌ها به صورت نوار وضعیت نمایش داده می‌شود.
- **پیام‌های مناسب:** در صورت وجود خطا یا موفقیت، پیام‌های مشخصی بدون تداخل با نوار وضعیت نمایش داده می‌شوند.

---

### **پیش‌نیازها**

1. **پایتون نسخه 3.6 یا بالاتر**
   - برای نصب پایتون: [Python.org](https://www.python.org)
2. **FFMPEG**
   - یک ابزار خط فرمان برای پردازش فایل‌های ویدیویی و صوتی.
   - می‌توانید آن را از [FFMPEG.org](https://ffmpeg.org/) دانلود و نصب کنید.
   - پس از نصب، مطمئن شوید مسیر `bin` مربوط به FFMPEG به متغیر محیطی `PATH` اضافه شده باشد.
3. **کتابخانه‌های پایتون**
   - کتابخانه `tqdm`: برای نمایش نوار پیشرفت.
   - کتابخانه `ffmpeg-python`: برای پشتیبانی از دستورات FFMPEG.
   - این کتابخانه‌ها به صورت خودکار توسط اسکریپت نصب می‌شوند.

---

### **ساختار فایل‌ها**

اطمینان حاصل کنید که فایل‌های ویدیویی و صوتی شما به این صورت ساختاردهی شده‌اند(همه در یک پوشه، نام ویدیو و صوت یکسان باشد):

```
├── video1.mp4
├── video2.mkv
├── video1.mp3
├── video2.mp3
```

- فایل‌های صوتی و ویدیویی باید نام مشابه داشته باشند (به جز پسوند).

---

### **نحوه استفاده**

1. **کلون یا کپی کردن پروژه:**

   ```bash
   git clone https://github.com/mohammad021/MergeMKV.git
   cd MergeMKV
   ```

2. **اجرا:**

   ```bash
   python mergmkv.py
   ```

3. **مراحل:**
   - اگر FFMPEG در سیستم شما نصب نشده باشد، اسکریپت از شما مسیر نصب آن را درخواست می‌کند.
   - اسکریپت فایل‌های ویدیویی و صوتی موجود در دایرکتوری جاری را بررسی و ادغام می‌کند.
   - فایل‌های خروجی در پوشه‌ای با نام `mkv` ذخیره می‌شوند.

---

### **موارد قابل بهبود**

- **پشتیبانی از فرمت‌های اضافی:** با کمی تغییر می‌توانید پشتیبانی از فرمت‌های دیگر مانند `.avi` یا `.flac` را اضافه کنید.
- **پیکربندی مسیرها:** امکان تنظیم مسیرهای ورودی و خروجی از طریق آرگومان خط فرمان.
- **گزارش خطا:** ذخیره خطاها در یک فایل جداگانه.

---

### **لایسنس**

این پروژه تحت لایسنس MIT منتشر می‌شود. 


### Documentation Explanation

---

## **MergeMKV: A Tool for Merging Video and Audio Files Using FFMPEG**

`MergeMKV` is a Python script that allows you to automatically merge related audio and video files and create MKV output files. This tool is specifically designed for environments where audio files (e.g., MP3) are stored separately from video files and need to be merged.

---

### **Features**

- **Automatic Merging:** Finds and merges video and audio files with matching names.
- **Format Support:** Supports video formats `.mp4` and `.mkv` and audio files `.mp3` by default.
- **Minimal Requirements:** Only requires Python and FFMPEG to be installed.
- **Progress Bar Display:** Displays the progress of file processing using `tqdm`.
- **Clear Messages:** Shows specific messages for errors or successes without interfering with the progress bar.

---

### **Prerequisites**

1. **Python 3.6 or higher**
   - To install Python: [Python.org](https://www.python.org)
2. **FFMPEG**
   - A command-line tool for processing video and audio files.
   - Download and install it from [FFMPEG.org](https://ffmpeg.org/).
   - Ensure the `bin` path of FFMPEG is added to the `PATH` environment variable after installation.
3. **Python Libraries**
   - `tqdm` library: For displaying progress bars.
   - `ffmpeg-python` library: For supporting FFMPEG commands.
   - These libraries are automatically installed by the script.

---

### **File Structure**

Ensure your video and audio files are structured as follows (all in one folder, with the video and audio names being the same except for the extension):

```
├── video1.mp4
├── video2.mkv
├── video1.mp3
├── video2.mp3
```

- Video and audio files must have matching names (excluding the extension).

---

### **Usage**

1. **Clone or Copy the Project:**

   ```bash
   git clone https://github.com/mohammad021/MergeMKV.git
   cd MergeMKV
   ```

2. **Run the Script:**

   ```bash
   python mergmkv.py
   ```

3. **Steps:**
   - If FFMPEG is not installed on your system, the script will ask you to provide its installation path.
   - The script will check and merge the available video and audio files in the current directory.
   - Output files will be stored in a folder named `mkv`.

---

### **Possible Improvements**

- **Additional Format Support:** Add support for other formats like `.avi` or `.flac` with slight modifications.
- **Path Configuration:** Allow input and output paths to be set via command-line arguments.
- **Error Reporting:** Save errors in a separate file.

---

### **License**

This project is released under the MIT License.

---

