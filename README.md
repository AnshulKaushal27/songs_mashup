# 🎵 Songs Mashup Generator

A locally deployed Streamlit-based application that automatically downloads popular songs of a given singer from YouTube, generates a custom mashup, and delivers the final output via email. This project demonstrates integration of:

- Web UI development
- Audio processing
- YouTube data extraction
- Email automation
- Local deployment architecture

---

## 🚀 Features

- 🎤 **Search songs by singer name**
- 🎶 **Select number of songs** (supports large batches)
- ⏱ **Custom duration per song** OR full-length option
- 🎧 **Automatic mashup generation**
- 📦 **ZIP file creation**
- 📧 **Automatic email delivery**
- 💾 **Manual download option** inside the app
- 🖥 **Fully local deployment** (no cloud restrictions)

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend / UI** | Streamlit |
| **YouTube Downloader** | yt-dlp |
| **Audio Processing** | pydub |
| **Email Protocol** | SMTP (Gmail App Password Authentication) |
| **Audio Backend** | FFmpeg |

---

## 🖼 Demo

<img width="1268" height="950" alt="Screenshot 2026-02-14 130558" src="https://github.com/user-attachments/assets/0ec1b5fc-f25d-4f12-b3fe-ff4a4f8e6287" />


The application features a clean, dark-themed interface with:
- Singer name input
- Adjustable number of songs slider
- Custom duration or full song options
- Output file naming
- Email delivery integration
- Real-time audio preview
- Download and email confirmation

---

## 📂 Project Structure

```
songs_mashup/
│
├── app.py              # Streamlit UI + Email integration
├── mashup.py           # YouTube download + Audio merging logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup (Local Deployment)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnshulKaushal27/songs_mashup.git
cd songs_mashup
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg

FFmpeg is required for audio extraction and merging.

**Windows:**
1. Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Download **Release Full**
3. Extract
4. Add `bin` folder to **Environment Variables → PATH**
5. Verify installation:
   ```bash
   ffmpeg -version
   ```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4️⃣ Configure Gmail App Password

This project uses Gmail SMTP for sending mashup ZIP files.

**Steps:**
1. Enable **2-Step Verification** in Google Account
2. Generate **App Password**:
   - App → Mail
   - Device → Windows Computer
3. Copy generated 16-character password
4. Update inside `app.py`:

```python
SENDER_EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "your_generated_app_password"
```

⚠ **Do NOT use your normal Gmail password.**

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in terminal.

---

## 🔄 How It Works

1. User enters **singer name**.
2. Application searches YouTube using `yt-dlp`.
3. Audio streams are downloaded and converted to MP3 using FFmpeg.
4. Selected segments are merged using `pydub`.
5. Final mashup is exported as:
   - `.mp3`
   - `.zip`
6. ZIP file is:
   - Available for direct download
   - Sent via email to the user

---

## 🧠 Technical Workflow

```
YouTube Search 
    → Audio Download 
    → MP3 Conversion 
    → Audio Segmentation 
    → Concatenation 
    → Export 
    → ZIP Packaging 
    → SMTP Email Delivery
```

---

## ⚠️ Deployment Notes

This project is designed for **local deployment only**.

Cloud platforms like:
- Render
- Railway
- Streamlit Cloud

may block YouTube scraping due to IP restrictions.

For demonstration and academic purposes, **local deployment is recommended**.

---

## 📈 Possible Enhancements

- [ ] Crossfade transitions between tracks
- [ ] Audio normalization
- [ ] Beat matching
- [ ] Background task queue
- [ ] Docker containerization
- [ ] Secure environment variable configuration
- [ ] Upload-based version for cloud deployment

---

## 🎓 Academic Use Case

This project demonstrates practical integration of:

- Media data scraping
- Audio signal manipulation
- Backend processing
- SMTP communication
- Interactive UI design

It can be extended into a full-fledged music processing system.

---

## 📜 Disclaimer

> **This project is intended for educational and demonstration purposes only.**
> 
> Users must ensure compliance with YouTube's terms of service and copyright policies.

---

## 📧 Contact

For questions or contributions, please open an issue or submit a pull request.

---

## 📝 License

This project is available under the MIT License.

---

**Made with ❤️ for learning and exploration**
