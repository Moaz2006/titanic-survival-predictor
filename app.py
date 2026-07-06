import streamlit as st
import requests

# إعدادات الصفحة والشكل
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")

st.title("🚢 نظام التوقع بنجاة ركاب تيتانيك")
st.write("أدخل بيانات الراكب واسمه أدناه لمعرفة احتمالية نجاته باستخدام الذكاء الاصطناعي.")

st.divider()

# عمل الفورم (Form) لتجميع البيانات من المستخدم
with st.form("passenger_form"):
    # 👈 ضيفنا خانة الاسم هنا في البداية عشان المستخدم يكتب فيها
    passenger_name = st.text_input("اسم الراكب (Passenger Name)", value="معاذ وائل")
    
    col1, col2 = st.columns(2)
    
    with col1:
        passenger_id = st.number_input("رقم الراكب (Passenger ID)", min_value=1, value=1, step=1)
        pclass = st.selectbox("درجة السفر (Pclass)", options=[1, 2, 3], index=0)
        age = st.number_input("العمر (Age)", min_value=0.0, max_value=100.0, value=22.0, step=0.5)
        
    with col2:
        sibsp = st.number_input("عدد الأشقاء/الزوجة على السفينة (SibSp)", min_value=0, value=0, step=1)
        parch = st.number_input("عدد الوالدين/الأبناء على السفينة (Parch)", min_value=0, value=0, step=1)
        sex = st.selectbox("الجنس (Sex)", options=["ذكر (Male)", "أنثى (Female)"], index=0)

    # تحويل الجنس لرقم يفهمه الموديل
    sex_encoded = 1 if sex == "ذكر (Male)" else 0

    # زرار الإرسال
    submitted = st.form_submit_button("توقع المصير 🔮", use_container_width=True)

# لما المستخدم يدوس على الزرار
if submitted:
    # تجهيز البيانات في شكل JSON (وبنبعت الاسم معاهم أهو)
    passenger_data = {
        "PassengerId": passenger_id,
        "Name": passenger_name,  # 👈 الاسم بيروح هنا للسيرفر
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Sex_1": sex_encoded
    }
    
    try:
        with st.spinner("جاري تحليل البيانات من السيرفر..."):
            # إرسال البيانات للـ API
            response = requests.post("http://127.0.0.1:8000/predict", json=passenger_data)
            result_json = response.json()
        
        st.divider()
        # عرض النتيجة المكتوب فيها الاسم جوه السيرفر
        if result_json["status"] == "نجاح":
            st.success(f"🎉 {result_json['result']}")
        else:
            st.error(f"💀 {result_json['result']}")
            
    except Exception as e:
        st.error("عفواً! تأكد من أن سيرفر الـ API شغال في الخلفية (uvicorn main:app).")