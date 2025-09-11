from langchain_core.messages import HumanMessage, SystemMessage

from state.state import ReportState
from ....schemas.schema import MedicalReportClassify, WellnessReport
from ....config import SYSTEM_PROMPT


class ReportNode:
    
    def __init__(self, model):
        self.llm = model
        
    ### Node 1
    def classify_report(self, state: ReportState):
        """
            Determine if the report text is medical and update the state.

            Args:
                state (ReportState): Contains 'report_text' key with the report content.

            Returns:
                ReportState: Updated state with 'report_status' indicating classification.
        """
        print("CLASSIFYING REPORT............")
        
        text = state["report_text"]
        
        llm_with_structure_output = self.llm.with_structured_output(MedicalReportClassify)
        output = llm_with_structure_output.invoke(text)
        
        state["report_status"] = output.check
    
        return state
    
    ### Node 2
    def generate_report(self, state: ReportState):
        """
            Generate a structured JSON wellness report from the report text.

            Args:
                state (ReportState): Contains 'report_text' key with the input text.

            Returns:
                ReportState: Updated state with 'output' key containing the JSON report.
        """
        print("GENERATING REPORT............")

        input_text = state["report_text"]
        
        llm_report_structure = self.llm.with_structured_output(WellnessReport)
        
        output = llm_report_structure.invoke([
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content = input_text)
        ])
        
        final_output = output.model_dump_json(indent=4)
        
        state["output"] = final_output
        
        return state
    
    ### Node 3
    def not_report(state: ReportState):
        """
            Handle cases where the input text is not a valid medical or lab report.

            Args:
                state (ReportState): The current state of the report processing.

            Returns:
                ReportState: Updated state with 'output' containing an error message.
        """
        print("NOT ACTUAL REPORT............")
        state["output"] = "The provided text does not appear to be a medical or lab report. Please upload a valid health report for analysis."
        
        return state
    
    ### decision function
    def router_decision(state: ReportState):
        """
            Decide the next action based on whether the report is medical.

            Args:
                state (ReportState): Contains 'report_status' key indicating classification.

            Returns:
                str: 'generate_report' if medical, otherwise 'not_report'.
        """
        if state['report_status'] == "yes":
            return "generate_report"
        else:
            return "not_report"