📊 Monitoring System (Django Dashboard)
📌 Loyihaning maqsadi

Ushbu loyiha universitet amaliy topshirig‘i sifatida ishlab chiqilgan bo‘lib, mahsulotlar (go‘sht, guruch va sut mahsulotlari) narxlarining oylar kesimidagi o‘zgarishini vizual diagrammalar orqali ko‘rsatadi.

⚙️ Texnologiyalar
Python 3
Django Framework
SQLite (default DB)
HTML / CSS / Bootstrap 5
JavaScript
Chart.js
📁 Loyihaning strukturasi
monitoring/
│
├── apps/
│   └── products/
│
├── templates/
│   ├── layout.html
│   ├── dashboard/
│   │   ├── meat_rice.html
│   │   └── milk.html
│
├── static/
│   ├── js/
│   │   ├── meat_rice.js
│   │   └── milk.js
│   ├── css/
│
├── config/
├── manage.py
📊 Funksiyalar
🥩 1-forma: Go‘sht va Guruch
Go‘sht va guruch mahsulotlari narxlari
Oylik o‘zgarishlar line chart orqali ko‘rsatiladi
Real-time DB’dan ma’lumot olinadi
🥛 2-forma: Sut mahsulotlari
Sut mahsulotlari narxlari
Oylik o‘sish/pasayish bar chart orqali ko‘rsatiladi
Chart.js orqali vizual tahlil
🧠 Model tuzilishi
Product – mahsulot nomi va kategoriyasi
MonthlyPrice – oy, yil va narx ma’lumotlari
🚀 O‘rnatish
1. Repository clone qilish
git clone <repo-url>
cd monitoring
2. Virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Requirements
pip install -r requirements.txt
4. Migratsiya
python manage.py makemigrations
python manage.py migrate
5. Serverni ishga tushirish
python manage.py runserver
🌐 Sahifalar
/ → Go‘sht va Guruch chart
/milk/ → Sut mahsulotlari chart
📈 Natija

Loyiha orqali:

Django ORM bilan ishlash
Template engine ishlatish
Chart.js bilan vizualizatsiya
Clean project structure

o‘rganiladi.
