from langgraph.graph import StateGraph, START, END

from ..state.state import ReportState
from ..nodes.node import ReportNode


class LabReportGraph:
    
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(ReportState)
        
    
    def setup_graph(self):
        
        self.report_node = ReportNode(self.llm)
        
        #### Add Node
        self.graph_builder.add_node("classify_report",self.report_node.classify_report)
        self.graph_builder.add_node("generate_report", self.report_node.generate_report)
        self.graph_builder.add_node("not_report", self.report_node.not_report)

        #### Add edges
        self.graph_builder.add_edge(START, "classify_report")
        self.graph_builder.add_conditional_edges(
            "classify_report",
            self.report_node.router_decision,
            {
                "generate_report" : "generate_report",
                "not_report" : "not_report"
            }
        )
        self.graph_builder.add_edge("generate_report", END)
        self.graph_builder.add_edge("not_report", END)

        graph = self.graph_builder.compile()
        
        return graph