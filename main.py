import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="DermNet",
    page_icon="🔍",
)

st.markdown(
    """
<style>
h1 {
    color: #D68D1C;
}
titke
</style>
""",
    unsafe_allow_html=True,
)



# Load the trained model
model = tf.keras.models.load_model('cnn.h5')
disease_info = [
    {
        "1": "Acne and Rosacea Photos",
        "Disease": "Acne and Rosacea Photos",
        "Overview": "Rosacea most commonly affects middle-aged women with fair skin. It can be mistaken for acne or other skin conditions. Key symptoms are facial redness with swollen red bumps and small visible blood vessels.",
        "Medical Treatments": "Benzoyl Peroxide, Salicylic Acid, tretinoin, adapalene, Antibiotics, Oral Contraceptives, Isotretinoin, Topical Metronidazole, Azelaic Acid, Topical Brimonidine, Oral Antibiotics, Isotretinoin.",
        "Home Remedies": "Gentle Cleansing, Honey, Tea Tree Oil, Aloe Vera, Apple Cider Vinegar, Green Tea, Gentle Skincare, Sun Protection, Cool Compresses, Oatmeal Baths, Licorice Extract, Chamomile."
    },
    {
        "2": "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions",
        "Disease": "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions",
        "Overview": "An actinic keratosis (ak-TIN-ik ker-uh-TOE-sis) is a rough, scaly patch on the skin that develops from years of sun exposure. It's often found on the face, lips, ears, forearms, scalp, neck or back of the hands.",
        "Medical Treatments": "Topical Medications, Cryotherapy, Chemical Peels, Photodynamic Therapy, Laser Therapy.",
        "Home Remedies": "Sun Protection, Skin Hydration."
    },
    {
        "3": "Actinic keratosis",
        "Disease": "Actinic Keratosis",
        "Overview": "An actinic keratosis (ak-TIN-ik ker-uh-TOE-sis) is a rough, scaly patch on the skin that develops from years of sun exposure. It's often found on the face, lips, ears, forearms, scalp, neck or back of the hands.",
        "Medical Treatments": "Topical Medications, Cryotherapy, Chemical Peels, Photodynamic Therapy, Laser Therapy.",
        "Home Remedies": "Sun Protection, Skin Hydration."
    },
    {
        "4": "Atopic Dermatitis Photos",
        "Disease": "Atopic Dermatitis Photos",
        "Overview": "Atopic dermatitis (eczema) is a condition that causes dry, itchy and inflamed skin. It's common in young children but can occur at any age. Atopic dermatitis is long lasting (chronic) and tends to flare sometimes. It can be irritating but it's not contagious.",
        "Medical Treatments": "Topical Corticosteroids, Topical Calcineurin Inhibitors, Topical Phosphodiesterase-4 Inhibitors, Oral Antihistamines, Topical or Oral Antibiotics, Wet Dressings.",
        "Home Remedies": "Moisturize, Avoid Irritants, Warm Baths,"
    },
    {
        "5": "Basal cell carcinoma",
        "Disease": "Basal Cell Carcinoma",
        "Overview": "Basal cell carcinoma is a type of skin cancer. Basal cell carcinoma begins in the basal cells \u2014 a type of cell within the skin that produces new skin cells as old ones die off.",
        "Medical Treatments": "Topical Chemotherapy, Topical Hedgehog Pathway Inhibitors, Systemic Hedgehog Pathway Inhibitors, Surgical Excision, Mohs Surgery, Electrodessication and Curettage, Cryotherapy, Laser Therapy."
    },
    {
        "6": "Benign Keratosis",
        "Disease": "Benign Keratosis",
        "Overview": "A seborrheic keratosis (seb-o-REE-ik ker-uh-TOE-sis) is a common noncancerous (benign) skin growth. People tend to get more of them as they get older. Seborrheic keratoses are usually brown, black or light tan. The growths (lesions) look waxy or scaly and slightly raised.",
        "Medical Treatments": "Cryotherapy, Curettage, Electrocautery, Laser Therapy, Topical Retinoids.",
        "Home Remedies": "Moisturizers, Alpha Hydroxy Acids (AHAs, Salicylic Acid, Tea Tree Oil, Apple Cider Vinegar."
    },
    {
        "7": "Bowens Disease",
        "Disease": "Bowens Disease",
        "Overview": "Bowen's disease is a very early form of skin cancer that's easily treatable. The main sign is a red, scaly patch on the skin. It affects the squamous cells, which are in the outer layer of skin, and is sometimes referred to as squamous cell carcinoma in situ.",
        "Medical Treatments": "Cryotherapy, Curettage and Electrodessication, Laser Therapy, Topical Chemotherapy, Photodynamic Therapy, Surgical Excision."
    },
    {
        "8": "Bullous Disease Photos",
        "Disease": "Bullous Disease Photos",
        "Overview": "Bullous pemphigoid (BUL-us PEM-fih-goid) is a rare skin condition that causes large, fluid-filled blisters. They develop on areas of skin that often flex \u2014 such as the lower abdomen, upper thighs or armpits. Bullous pemphigoid is most common in older adults.",
        "Medical Treatments": "Corticosteroids, Immune-Suppressing Medications, Antibiotics or Antiviral Drugs, Immunomodulators, Biologics, Wound Care.",
        "Home Remedies": "Cleanliness, Avoid Irritants, Cool Compresses, Oatmeal Baths, Loose Clothing, Hydration."
    },
    {
        "9": "Cellulitis Impetigo and other Bacterial Infections",
        "Disease": "Cellulitis Impetigo and other Bacterial Infections",
        "Overview": "Impetigo is a non-life-threatening infection, but can result in post-streptococcal acute glomerulonephritis (AGN). Cellulitis and erysipelas can be mild or moderately severe, while necrotizing fasciitis, myonecrosis and StrepTSS are life-threatening.",
        "Medical Treatments": "Antibiotics (Penicillins, Cephalosporins,",
        "Home Remedies": "Warm Compress, Elevate the Area, Pain Relief, Hygiene, Avoid Scratching, Proper Wound Care, Nutrition and Hydration."
    },
    {
        "10": "Dermatofibroma",
        "Disease": "Dermatofibroma",
        "Overview": "Dermatofibroma is a commonly occurring cutaneous entity usually centered within the skin's dermis. Dermatofibromas are referred to as benign fibrous histiocytomas of the skin, superficial/cutaneous benign fibrous histiocytomas, or common fibrous histiocytoma.",
        "Medical Treatments": "Surgical Excision, Cryotherapy.",
        "Home Remedies": "Moisturizing, Avoid Scratching, Topical Steroids, Warm Compress, Salicylic Acid."
    },
    {
        "11": "Eczema Photos",
        "Disease": "Eczema Photos",
        "Overview": "Eczema is a skin condition that causes dry and itchy patches of skin. It's a common condition that isn't contagious. Symptoms of eczema can flare up if you contact an irritant or an allergen. There are treatments available to help you manage symptoms, but there isn't a cure.",
        "Medical Treatments": "Topical Corticosteroids, Topical Calcineurin Inhibitors, Topical Phosphodiesterase-4 Inhibitors, Oral Antihistamines, Topical Immune Modulators, Wet Dressings, Oral Steroids.",
        "Home Remedies": "Moisturize, Avoid Irritants, Cool Compresses, Cotton Clothing, Short, Lukewarm Baths, Humidifier."
    },
    {
        "12": "Exanthems and Drug Eruptions",
        "Disease": "Exanthems and Drug Eruptions",
        "Overview": "The most common type of EDEs is maculopapular rash (MPR) that is characterized by erythematous macules evolving in papules from 1 to 5 mm in diameter and may coalesce in plaques. MPR involves face, neck, or upper trunk and tipically spreads bilaterally and symmetrically toward the limbs.",
        "Medical Treatments": "Antibiotics or Antiviral Medications, Supportive Care, Discontinuation of the Offending Medication Topical Steroids, Oral Antihistamines, Systemic Corticosteroids.",
        "Home Remedies": "Cool Compresses, Hydration, Avoid Scratching, Avoid Triggers, Cotton Clothing."
    },
    {
        "13": "Hair Loss Photos Alopecia and other Hair Diseases",
        "Disease": "Hair Loss Photos Alopecia and other Hair Diseases",
        "Overview": "Alopecia areata is an autoimmune condition, which means the body's immune system attacks healthy tissues, including the hair follicles. This causes hair to fall out and prevents new hair from growing. This condition can affect adults and children, and hair loss can begin suddenly and without warning.",
        "Medical Treatments": "Minoxidil, Finasteride, Corticosteroids, Topical Immunotherapy, Platelet-Rich Plasma (PRP) Therapy, Hair Transplant.",
        "Home Remedies": "Healthy Diet, Scalp Massage, Gentle Hair Care, Stress Management, Avoid Overprocessing, Aloe Vera."
    },
    {
         "14": "Herpes HPV and other STDs Photos",
        "Disease": "Herpes HPV and other STDs Photos",
        "Overview": "Human papillomavirus (HPV) and herpes are both common viruses that can be transmitted sexually. Herpes and HPV have many similarities, meaning some people might be unsure which one they have. HPV and herpes can both cause genital lesions, but they can also both present without symptoms. Although similar, HPV is much more common than herpes. In fact, nearly allTrusted Source sexually active people will have HPV at least once in their lives. But for anyone who is sexually active, it\u2019s possible to contract one or both of these viruses at some point.",
        "Medical Treatments": "cyclovir, Valacyclovir, Famciclovir, Removal of genital warts, Vaccination to prevent certain types of HPV that cause cancer, Bacterial STDs (e.g., Chlamydia, Gonorrhea, Syphilis), Viral STDs (e.g., HIV, Hepatitis B and C).",
        "Home Remedies": "Safe Sex Practices, Regular Testing, Vaccinations, Good Hygiene, Avoidance of High-Risk Behaviors."
    },
    {
        "15": "Light Diseases and Disorders of Pigmentation",
        "Disease": "Light Diseases and Disorders of Pigmentation",
        "Overview": "Pigmentation- Abnormal Pigmentation. Birthmarks and other pigmentation disorders affect many people. Some of the most common are pigmented birthmarks, macular stains, hemangiomas, port wine stains, while disorders include albinism, melasma, vitiligo and pigmentation loss due to skin damage.",
        "Medical Treatments": "Topical Hydroquinone, Topical Retinoids, Chemical Peels, Laser Therapy, Topical Steroids, Topical Calcineurin Inhibitors, Narrowband UVB Phototherapy.",
        "Home Remedies": "Sun Protection, Exfoliation,Topical Vitamin C."
    },
    {
        "16": "Lupus and other Connective Tissue diseases",
        "Disease": "Lupus and other Connective Tissue diseases",
        "Overview": "A connective tissue disease is any disease that affects the parts of the body that connect the structures of the body together. Connective tissues are made up of two proteins: collagen and elastin. Collagen is a protein found in the tendons, ligaments, skin, cornea, cartilage, bone and blood vessels. Elastin is a stretchy protein that resembles a rubber band and is the major component of ligaments and skin. When a patient has a connective tissue disease, the collagen and elastin are inflamed. The proteins and the body parts they connect are harmed.",
        "Medical Treatments": "Non-Steroidal Anti-Inflammatory Drugs (NSAIDs), Corticosteroids, Immunosuppressive Drugs, Biologic Therapies, Disease-Modifying Antirheumatic Drugs (DMARDs), Biologic Therapies, Symptomatic Relief.",
        "Home Remedies": "Rest and Stress Management, Exercise, Healthy Diet, Hydration."
    },
    {
        "17": "Melanocytic nevi",
        "Disease": "Melanocytic Nevi",
        "Overview": "Giant congenital melanocytic nevus is a skin condition characterized by an abnormally dark, noncancerous skin patch (nevus) that is composed of pigment-producing cells called melanocytes. It is present from birth (congenital) or is noticeable soon after birth.",
        "Medical Treatments": "Observation, Surgical Removal.",
        "Home Remedies": "Sun Protection, Skin Hydration."
    },
    {
        "18": "Melanoma",
        "Disease": "Melanoma",
        "Overview": "Melanoma is a disease in which malignant (cancer) cells form in melanocytes (cells that color the skin). There are different types of cancer that start in the skin. Melanoma can occur anywhere on the skin. Unusual moles, exposure to sunlight, and health history can affect the risk of melanoma.",
        "Medical Treatments": "Surgical Removal, Lymph Node Biopsy,",
        "Home Remedies": "Sun Protection, Healthy Lifestyle, Support Networks."
    },
    {
        "19": "Melanoma Skin Cancer Nevi and Moles",
        "Disease": "Melanoma Skin Cancer Nevi and Moles",
        "Overview": "People with many moles or unusual moles called dysplastic nevi or atypical moles have a higher risk of developing melanoma. Dysplastic nevi are large moles that have irregular color and shape. A doctor may recommend regular photography of the skin to closely watch the skin of people with many moles.",
        "Medical Treatments": "Surgical Removal, Lymph Node Biopsy, Immunotherapy, Targeted Therapy, Radiation Therapy.",
        "Home Remedies": "Sun Protection, Skin Hydration."
    },
    {
        "20": "Nail Fungus and other Nail Disease",
        "Disease": "Nail Fungus and other Nail Disease",
        "Overview": "Nail fungus is caused by various fungal organisms (fungi). The most common is a type called dermatophyte. Yeast, bacteria and molds also can cause nail infections. The discoloration from a bacterial infection tends to be green or black.",
        "Medical Treatments": "Topical Antifungals, Oral Antifungal Medications, Laser Therapy, Surgical Removal, Paronychia (Nail Infection), Ingrown Toenails, Psoriasis or Eczema of the Nails.",
        "Home Remedies": "Good Nail Hygiene, Avoid Trauma, Comfortable Footwear."
    },
    {
        "21": "Poison Ivy Photos and other Contact Dermatitis",
        "Disease": "Poison Ivy Photos and other Contact Dermatitis",
        "Overview": "When the skin comes in direct contact with an irritating or allergy-causing substance, contact dermatitis can develop. Exposure to poison ivy, poison oak, and poison sumac causes more cases of allergic contact dermatitis than all other plant families combined.",
        "Medical Treatments": "Topical Corticosteroids, Cool Compresses, Calamine Lotion, Oral Antihistamines, Avoid Scratching.",
        "Home Remedies": "Cool Baths, Avoid Irritants, Hydration, Aloe Vera Gel."
    },
    {
        "22": "Psoriasis Pictures Lichen Planus and related diseases",
        "Disease": "Psoriasis pictures Lichen Planus and related diseases",
        "Overview": "Lichen planus and psoriasis can both cause skin changes, but have different causes and treatments. Psoriasis is an autoimmune condition, but the cause of lichen planus remains unclear. Both lichen planus and psoriasis can cause patches of scaly bumps or rashes on the skin.",
        "Medical Treatments": "Topical Corticosteroids, Topical Vitamin D Analogues, Topical Retinoids, Topical Calcineurin Inhibitors, Phototherapy, Systemic Medications, Topical Corticosteroids, Topical Calcineurin Inhibitors, Oral Medications.",
        "Home Remedies": "Moisturizing, Avoid Irritants, Stress Management, Healthy Diet."
    },
    {
         "23": "Scabies Lyme Disease and other Infestations and Bites",
        "Disease": "Scabies Lyme Disease and other Infestations and Bites",
        "Overview": "Scabies is caused by the human itch mite (Sarcoptes scabiei), a tiny, eight-legged parasite that burrows into the upper layer of the skin in order to feed and live. Female mites also lay eggs there. When this happens, the skin often breaks out into an itchy, pimple-like rash in an allergic reaction to the mites, their eggs, and their waste.",
        "Medical Treatments": "Permethrin Cream, Ivermectin, Antibiotics.",
        "Home Remedies": "Wash the Area, Cool Compresses, Over-the-Counter Creams, Oral Antihistamines."
    },
    {
        "24": "Seborrheic Keratoses and other Benign Tumors",
        "Disease": "Seborrheic Keratoses and other Benign Tumors",
        "Overview": "Seborrheic keratosis is caused by the benign proliferation of immature keratinocytes, resulting in well-demarcated, round or oval, flat-shaped macules. They are typically slow-growing, can increase in thickness over time, and they rarely resolve spontaneously.",
        "Medical Treatments": "Cryotherapy, Electrocautery, Curettage, Excision, Laser Therapy.",
        "Home Remedies": "Sun Protection, Good Skin Care, Regular Self-Checks."
    },
    {
        "25": "Systemic Disease",
        "Disease": "Systemic Disease",
        "Overview": "Systemic means affecting the entire body, rather than a single organ or body part. For example, systemic disorders, such as high blood pressure, or systemic diseases, such as influenza (the flu), affect the entire body. An infection that is in the bloodstream is called a systemic infection.",
        "Medical Treatments": "Medications, Biologic Therapies, Chemotherapy and Radiation, Surgery, Lifestyle Modifications.",
        "Home Remedies": "Healthy Lifestyle, Hydration, Medication Adherence."
    },
    {
        "26": "Tinea Ringworm Candidiasis and other Fungal Infections",
        "Disease": "Tinea Ringworm Candidiasis and other Fungal Infections",
        "Overview": "Ringworm is a common infection of the skin and nails that is caused by fungus. The infection is called \u201cringworm\u201d because it can cause an itchy, red, circular rash. Ringworm is also called \u201ctinea\u201d or \u201cdermatophytosis.\u201d The different types of ringworm are usually named for the location of the infection on the body.",
        "Medical Treatments": "Antifungal Creams, Oral Antifungal Medications.",
        "Home Remedies": "Proper Hygiene, Air Circulation, Antifungal Powders, Yogurt, Keep the Area Dry, Avoid Sharing Personal Items, Good Hygiene, Dietary Changes."
    },
    {
        "27": "Urticaria Hives",
        "Disease": "Urticaria Hives",
        "Overview": "Hives is also called urticaria. Hives \u2014 also called urticaria (ur-tih-KAR-e-uh) \u2014 is a skin reaction that causes itchy welts. Chronic hives are welts that last for more than six weeks and return often over months or years. Often, the cause of chronic hives isn't clear.",
        "Medical Treatments": "Antihistamines, Corticosteroids, Epinephrine, Immunosuppressants.",
        "Home Remedies": "Cool Compresses, Avoid Triggers, Avoid Tight Clothing, Hydration."
    },
    {
        "28": "vascular lesions",
        "Disease": "Vascular Lesions",
        "Overview": "Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks. There are three major categories of vascular lesions: Hemangiomas, Vascular Malformations, and Pyogenic Granulomas.",
        "Medical Treatments": "Laser Therapy, Sclerotherapy, Embolization, Surgical Removal.",
        "Home Remedies": "Sun Protection, Good Skin Care."
    },
    {
        "29": "Vascular Tumors",
        "Disease": "Vascular Tumors",
        "Overview": "Rare vascular tumors form in cells that make blood or lymph vessels. They can occur anywhere in the body, such as the skin, in the tissues below the skin, or in an organ. These tumors are named for the type of cells they look like and how they grow.",
        "Medical Treatments": "Corticosteroids, Laser Therapy, Embolization, Surgery.",
        "Home Remedies": "Sun Protection, Good Skin Care."
    },
    {
         "30": "Vasculitis Photos",
        "Disease": "Vasculitis Photos",
        "Overview": "Vasculitis is an inflammation of the blood vessels. It happens when the body's immune system attacks the blood vessel by mistake. It can happen because of an infection, a medicine, or another disease. The cause is often unknown. Vasculitis can affect arteries, veins and capillaries.",
        "Medical Treatments": "Corticosteroids, Immunosuppressive Drugs, Biologic Therapies, Plasma Exchange (Plasmapheresis).",
        "Home Remedies": "Rest, Healthy Diet, Stress Management."
    },
    {
        "31": "Warts Molluscum and other Viral Infections",
        "Disease": "Warts Molluscum and other Viral Infections",
        "Overview": "Molluscum contagiosum is a viral skin infection that causes one or many raised, pearl-like bumps (papules) on your skin. Papules may persist from a few months to a few years. The condition easily spreads (contagious). Treatment helps the infection go away but isn't always necessary, as it can also go away on its own.",
        "Medical Treatments": "Salicylic Acid, Cryotherapy, Electrocautery, Prescription Medications, Laser Therapy, Self-Resolution, Curettage, Topical Treatments.",
        "Home Remedies": "Good Hygiene, Avoid Sharing Personal Items, Boost Immune System."
    },
    {
        "32": "No Disease Found",
        "Disease": "No Disease Found",
        "Overview": "Maintaining healthy skin is essential Even if you don't have any specific skin diseases, adopting a good skincare routine and healthy lifestyle habits can help keep your skin looking and feeling its best. Here are some home remedies of how to maintain healthy skin",
        "Home Remedies": "Cleansing, Limit Sun Exposure, Stay Hydrated, Take Health Precautions, Use Gentle Skin Care Products, Know Your Skin, Regular Checkups."
    }
]
class_names = ['Acne and Rosacea Photos','Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions','Actinic keratosis','Atopic Dermatitis Photos','Bullous Disease Photos','Cellulitis Impetigo and other Bacterial Infections','Eczema Photos','Exanthems and Drug Eruptions','Hair Loss Photos Alopecia and other Hair Diseases','Herpes HPV and other STDs Photos','Light Diseases and Disorders of Pigmentation','Lupus and other Connective Tissue diseases','Melanoma Skin Cancer Nevi and Moles','Nail Fungus and other Nail Disease','No Disease Found','Poison Ivy Photos and other Contact Dermatitis','Psoriasis pictures Lichen Planus and related diseases','Scabies Lyme Disease and other Infestations and Bites','Seborrheic Keratoses and other Benign Tumors','Systemic Disease','Tinea Ringworm Candidiasis and other Fungal Infections','Urticaria Hives','Vascular Tumors','Vasculitis Photos','Warts Molluscum and other Viral Infections','Basal Cell Carcinoma','Benign Keratosis', 'Dermatofibroma', 'Melanocytic Nevi', 'Melanoma', 'Vascular Lesions']

def get_disease_info(disease_name):
    for disease in disease_info:
        if disease['Disease'] == disease_name:
            return disease
    return None
def main():
    st.markdown("<h1>DermNet</h1>", unsafe_allow_html=True)
    # Create the custom option menu with vertical orientation in the sidebar
    with st.sidebar:
        logo = 'logo.png' 
        st.image(logo, width=200)
        selected_tab = option_menu(
            menu_title="Menu",
            options=['🏠 Home', '📝 About Us', '🔮 Prediction'],
            default_index=0,
            orientation="vertical",
        )
    # st.markdown(
    #     """
    #     <style>
    #     .sidebar .radio label span {
    #         font-size: 10px;
    #         font-weight: bold;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    # selected_tab = st.sidebar.radio('MENU', list(tab_options.keys()))

    # Handle navigation based on selected tab
    if selected_tab == '🏠 Home':
        st.header("🏠 Home")
        st.header("Embrace Radiant Skin with Dermnet: Your Skin Wisard")
        st.write(
            "Step into the world of Dermnet, where enchantment meets precision in skin diagnosis. A wondrous fusion of cutting-edge"
            " technology and the art of dermatology, Dermat is your steadfast companion on your journey to unveil the secrets"
            " beneath your skin."
        )
    
        st.write("## Embark on an Odyssey of Features")
        st.markdown(
            "- **Enigmatic Accuracy:** At the heart of Dermnet lies a constellation of intricate algorithms, crafting forecasts"
            " with astonishing precision, unlocking the mysteries of myriad skin conditions."
        )
        st.markdown(
            "- **Elegance Meets Intuition:** Ingeniously designed for all to embrace, Dermnet boasts a harmonious interface,"
            " resonating with the core of human intuition. You need not wield the scepter of technical prowess to wield its"
            " brilliance."
        )
        st.markdown(
            "- **A Sanctuary of Privacy:** Your trust is our sacred promise. Within the hallowed chambers of Dermnet, your personal"
            " saga remains guarded, your medical odyssey a tale shared only with your chosen guides."
        )
        st.markdown(
            "- **Universality Unleashed:** Whether beneath the stars or under the golden sun, Dermnet accompanies you, your loyal"
            " soothsayer, wherever your path may lead."
        )
    
        st.write("## Envisioning the Unveiling")
        st.markdown(
            "Embarking upon the journey with Dermnet is simple. Just breathe life into your queries by bestowing upon it an image,"
            " and watch as the celestial algorithm orchestrates a spellbinding prediction of your skin's narrative."
        )
    
        st.write("## The Magic of its Craft")
        st.markdown(
            "Dermant beckons the arcane powers of deep learning, deciphering the subtle dances of every pixel. The image is woven"
            " into a tapestry of understanding, as the algorithm delves into the vast compendium of its skin secrets to unveil its"
            " true essence."
        )
    
        st.write("## For Both Sage and Seeker")
        st.markdown(
            "Dermnet's allure embraces every wanderer on the path of skin enlightenment. Whether you are a venerable sage of"
            " dermatology, seeking a companion in diagnosis, or an intrepid seeker eager to decipher your skin's riddles, Dermnet"
            " extends its wisdom to all."
        )
    
        st.write("## Unveil the Magic of Dermnet Today!")
        st.markdown(
            "The tapestry of your skin's story awaits your touch. Cast your image upon the ethereal waters of Dermnet and watch as"
            " the reflection reveals the truth. Emerge with newfound insights and let Dermnet be your guide on this radiant journey."
        )
      
    elif selected_tab == '🔮 Prediction':
        st.header("🔮Prediction")
        image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
        try:
            if image is not None:
                img = Image.open(image)
                img_displa=img
                img = img.resize((64, 64))
                img_array = np.array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)
                dpi = 96  # Example DPI value, adjust as needed
                cm_to_inch = 5 / 2.54
                pixel_width = int(cm_to_inch * dpi)
                img1 = img.resize((pixel_width, pixel_width))
                predictions = model.predict(img_array)
                predicted_class = np.argmax(predictions[0])
                prediction_result = class_names[predicted_class]
                info = get_disease_info(prediction_result)
                st.image(img_displa, width=200)  
                if info is not None:
                    st.write(f"<span style='color: red; font-weight: bold;'>Please Consult a Doctor</span>", unsafe_allow_html=True)

                    st.write(f"<span style='font-weight: bold;'>Prediction:</span> {prediction_result}", unsafe_allow_html=True)
                    st.write(f"Overview: {info['Overview']}")
                    st.write(f"Overview: {info['Medical Treatments']}")
                    st.write(f"Home Remedies: {info['Home Remedies']}")
                else:
                    st.write(f"<span style='color: red; font-weight;'>Nothing to worry", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    elif selected_tab == '📝 About Us':
        st.header("📝About Us")
        st.header("Architects of Enchantment")
        st.write(
            "Behind the mystical curtain of Dermat stand three visionary architects, enchanters of code and conjurers of"
            " machine learning. Allow us to introduce the masterminds who have woven their dreams and aspirations into the"
            " very fabric of this realm."
        )
    
        st.write("## Meet the Architects of DermNet")
        st.markdown(
            "🔮 **Dinesh R:** A sorcerer with a fervor for machine learning, Dinesh weaves intricate spells of algorithms and"
            " data science. Currently embarking on a journey through the realms of 2nd year MCA at Christ (Deemed to be University),"
            " his fascination with the art of prediction led him to carve his path as a ML mystic."
        )
        st.markdown(
            "🌟 **Rahul V:** A celestial wanderer navigating the constellations of data, Rahul, too, walks the corridors of the"
            " 2nd year MCA realm at Christ (Deemed to be University). With a heart pulsating for machine learning and competitions,"
            " he's the North Star guiding our team's course."
        )
        st.markdown(
            "⚡ **Dishanth P:** A technomancer with an insatiable curiosity, Dishanth strides through the 2nd year MCA realm"
            " at Christ (Deemed to be University). With a keen affinity for unraveling complex algorithms, he is the lightbearer"
            " of our pursuit of knowledge."
        )
    
        st.write("## Enchanted by Knowledge, United by Dreams")
        st.markdown(
            "A confluence of destiny brought these three luminaries together, ignited by a shared passion for machine learning and"
            " the yearning to immerse themselves in its enchanting waters. United by dreams, they stand as the architects of Dermat,"
            " harnessing their magic to create a platform that harmonizes technology with humanity."
        )
    
        st.write("## Illuminating the Path Forward")
        st.markdown(
            "In this realm of ceaseless learning, these three visionaries seek not just to conjure predictions, but to cast spells"
            " of empowerment. Their mantra echoes in the corridors of code: 'To learn is to grow, and to grow is to illuminate the"
            " path for all.' Join them as they script their saga of evolution, enlightenment, and endless fascination."
        )
 
if __name__ == '__main__':
    main()
