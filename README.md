<h1> Chest X-Ray Pneumonia Detection</h1>
<p><b>A Deep Learning Web App for Pneumonia Classification using FastAPI</b></p>

<hr>

<h2> Overview</h2>
<p>This project detects <b>Pneumonia from Chest X-Ray images</b> using a <b>Deep Learning Sequential model</b>.<br>
The model is saved as <code>.keras</code> file and the app uses <b>FastAPI</b> to provide a simple web interface.<br>
Users can upload an image and get real-time predictions directly from the browser.</p>

<hr>

<h2> Features</h2>
<ul>
<li>✅ Deep Learning model trained on Chest X-Ray dataset</li>
<li>✅ FastAPI web app for real-time predictions</li>
<li>✅ Simple user-friendly interface (<code>index.html</code>)</li>
<li>✅ Binary classification: Pneumonia / Normal</li>
<li>✅ Easy to run, beginner-friendly</li>
</ul>

<hr>

<h2> Technologies Used</h2>
<p>
<img src="https://img.shields.io/badge/Python-3.11-blue">
<img src="https://img.shields.io/badge/TensorFlow-2.13-orange">
<img src="https://img.shields.io/badge/FastAPI-0.102-green">
<img src="https://img.shields.io/badge/Keras-2.14-red">
</p>
<ul>
<li>Python</li>
<li>TensorFlow / Keras</li>
<li>FastAPI</li>
<li>Jinja2 Templates</li>
<li>HTML / Tailwind CSS</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
chest-xray-pneumonia-detection/
│
├── code/
│    └── chest_xray_project.ipynb
│
├── model/
│    └── chest_xray_model.keras
│
├── templates/
│    └── index.html
│
├── app.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2> Installation & Run Guide</h2>

<h3>1️⃣ Clone the repository</h3>
<pre>
git clone https://github.com/AzeemAIDev/chest-xray-pneumonia-detection.git
</pre>

<h3>2️⃣ Navigate to the project folder</h3>
<pre>
cd chest-xray-pneumonia-detection
</pre>

<h3>3️⃣ Install the requirements</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Run the FastAPI app</h3>
<pre>
uvicorn app:app --reload --port 8800
</pre>

<h3>5️⃣ Open the Web Interface</h3>
<p>After running the app, open the browser and go to:</p>
<pre>
http://127.0.0.1:8800/
</pre>
<p>The <code>index.html</code> is served via FastAPI:</p>
<pre>
@app.get("/", response_class=HTMLResponse)
async def server_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
</pre>

<hr>

<h2> Model Information</h2>
<ul>
<li><b>Model Type:</b> Sequential Deep Learning Model</li>
<li><b>Task:</b> Binary Classification (Pneumonia / Normal)</li>
<li><b>Saved As:</b> chest_xray_model.keras</li>
</ul>

<p><b>Model Architecture (Placeholder Diagram):</b></p>
<img src="https://via.placeholder.com/600x300.png?text=Model+Architecture" width="600"/>

<hr>

<h2>📊 Dataset</h2>
<ul>
<li><b>Dataset:</b> Chest X-Ray Images (Pneumonia Dataset)</li>
<li><a href="https://www.kaggle.com/datasets/umitka/chest-x-ray-balanced" target="_blank">Kaggle Dataset Link</a></li>
</ul>


<hr>

<h2>⭐ Author</h2>
<p><b>Muhammad Azeem</b><br>
Machine Learning Engineer & AI Learner<br>
GitHub: <a href="https://github.com/AzeemAIDev" target="_blank">AzeemAIDev</a></p>
