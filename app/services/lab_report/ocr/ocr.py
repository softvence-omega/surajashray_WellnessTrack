from doctr.models import ocr_predictor
from doctr.io import DocumentFile

from app.utils.logger import get_logger

logger = get_logger(__name__)


class OCR:
    
    def __init__(self):
        pass
    
    @staticmethod
    def format_text(text) -> str:
        all_text = []
        
        for page in text["pages"]:
            for block in page["blocks"]:
                for line in block["lines"]:
                    line_text = " ".join([word["value"] for word in line["words"]])
                    all_text.append(line_text)
                    
        final_text = " ".join(all_text)
        return final_text
    
    # for pdf file
    def pdf_to_text(self, pdf_file) -> str:
        
        try:
            logger.info("OCR Model Start Downloading..........")
            self.model = ocr_predictor(det_arch="db_resnet50",reco_arch="crnn_mobilenet_v3_large",pretrained=True)
            logger.info("OCR Model Download Completed..........")
            self.pdf = DocumentFile.from_pdf(pdf_file)
            self.result = self.model(self.pdf)
            self.result = self.result.export()

            self.final_text = self.format_text(self.result)
            
            return self.final_text
        except Exception as e:
            raise ValueError(e)
        
    # for img file
    def img_to_text(self, img_file) -> str:     
        try:
            logger.info("OCR Model Start Downloading..........")
            self.model = ocr_predictor(det_arch="db_resnet50",reco_arch="crnn_mobilenet_v3_large",pretrained=True)
            logger.info("OCR Model Download Completed..........")
            self.img = DocumentFile.from_images(img_file)
            self.result = self.model(self.img)
            self.result = self.result.export()

            self.final_text = self.format_text(self.result)
            
            return self.final_text
        except Exception as e:
            raise ValueError(e)
        
        