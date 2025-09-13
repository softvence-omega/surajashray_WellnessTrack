# from app.services.lab_report.llms.onenai_llm import OpenAILLM
# from app.services.lab_report.graph.graph import LabReportGraph


# full_text = "TATA IMG Technologies Pvt. Ltd TATA LABORATORY: Ground Floor, Shop! No2 20 and 3, REGISTERED OFFICE: Plot Nol 156, Binori Ambit, Town Planning LEVEL 3, Vasant Square Mall, Schemer no: 38,Mouje Village Thaltej, Pocket V, Sector B, Taluka- Ghatlodiya, Ahmedabad, Gujarat, 380054 Vasant Kunj New Delhi 110070 1mg Labs www.lmg.com/labs N care@lmg.com CIN:U74140DL2015PTC279229 POI No: PO3469981132-641 Name : M.MANISHLODHA Client Name : TATA IMG. AHMEDABAD Age/Gender 48/Male DOB: Registration Date : 13-Apr-23 10:46 AM Patient ID AMD23701 Collection Date : 13/Apr/2023 06:29AM Barcode ID/Order ID D2014178. / 7043735 Sample Receive Date : 14/Apr/2023 08:44AM Referred By Dr. Report Status Final Report Sample' Type Whole Blood-EDTA Report Date . 14/Apr/2023 10:45AM HAEMATOLOGY COMPREHENSIVE GOLD FULL BODY CHECKUP Test Name Result Unit Bio. Ref. Interval Method Complete Blood Count Hemoglobin 15.6 g/dL 13.0-17.0 Cyanide free SLS RBC 5.16 106/cu.mm 4.5-5.5 Impedence variation HCT 44.6 % 40-50 Pulse Height Average MCV 86.5 fl 83-101 Calculated MCH 30.3 pg 27-32 Calculated MCHC 35.0 g/dL 31.5-34.5 Calculated RDW-CV 16.2 % 11.6-14 Calculated Total Leucocyte Count 6.26 1003/pI 4-10 Flowmetry DHSS/ Microscopy Differential Leucocyte Count Neutrophils 55.0 % 40-80 Flowcytometry DHSS/ Microscopy Lymphocytes 34.0 % 20-40 Flowcytometry DHSS/ Microscopy Monocytes 9.0 % 1-10 Flowcytometry DHSS/ Microscopy Eosinophils 2.0 % 1-6 Floweytometry DHSS/ Microscopy Basophils 0.0 % 0-2 Floweytometry DHSS/ Microscopy Absolute Leucocyte Count Absolute Neutrophil Count 3.44 103/I 2-7 Calculated Absolute Lymphocyte Count 2.13 103/uI 1-3 Calculated Absolute Monocyte Count 0.56 103/uI 0.1-1 Calculated Absolute Eosinophil Count 0.13 1003/pI 0.02-0.5 Calculated Absolute Basophil Count 0 103/uI 0.02-0.1 Calculated Platelet Count 281 103/uI 150-410 Impedence Variation Microscopy MPV 10.2 fl 6.5-12 Calculated PDW 16 fl 11-22 Calculated DM Dr. Chitral Kothari MBBS, MD (Pathology) Consultant Pathologist Reg No: G-22953 Page 2 of 22 ISO 9001:2015"
# ### LLM model init

# llm_model = OpenAILLM()
# llm = llm_model.get_llm_model()


# ### Graph init
# graph = LabReportGraph(model=llm)

# graph_builder = graph.setup_graph()

# result = graph_builder.invoke({
#     "report_text" : "Hello How are you?"
# })

# print(result["output"])


## OCR
# from app.services.lab_report.ocr.ocr import OCR

# # pdf_path = "temp_data/cbc_report.pdf"
# img_path = "temp_data/report_img.png"

# ocr = OCR()

# # print(ocr.pdf_to_text(pdf_path))
# print(ocr.img_to_text(img_path))


## api
from fastapi import FastAPI
import uvicorn

from app.api.v1.endpoints import lab_report

app = FastAPI()


app.include_router(lab_report.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)


