from agents.planner import Planner
from agents.executor import Executor
from agents.synthesizer import Synthesizer
from agents.verifier import Verifier
from agents.report_generator import ReportGenerator

from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from memory.episodic import EpisodicMemory

from tools.tool_registry import ToolRegistry
from tools.company_tool import CompanyTool
from tools.financial_tool import FinancialTool
from tools.news_tool import NewsTool
from tools.sec_tool import SECTool
from utils.report_saver import save_report
import ast


class FinancialResearchAgent:

    def __init__(self):

        # Agents
        self.planner = Planner()
        self.synthesizer = Synthesizer()
        self.verifier = Verifier()
        self.report_generator = ReportGenerator()

        # Memory
        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory()
        self.episodic_memory = EpisodicMemory()

        # Tool Registry
        registry = ToolRegistry()

        registry.register(CompanyTool())
        registry.register(FinancialTool())
        registry.register(NewsTool())
        registry.register(SECTool())

        self.executor = Executor(registry)

    def run(self, ticker, query):

        print("Planning...")

        plan = self.planner.create_plan(query)

        plan = ast.literal_eval(plan)

        print("Executing tools...")

        results = self.executor.execute_plan(plan, ticker)

        self.short_memory.store("results", results)

        print("Synthesizing...")

        analysis = self.synthesizer.synthesize(results)

        print("Verifying...")

        verification = self.verifier.verify(
            results,
            analysis
        )

        print("Generating report...")

        report = self.report_generator.generate_report(
            analysis,
            verification
        )

        self.long_memory.store(
            ticker,
            report
        )

        self.episodic_memory.add_episode(
            company=ticker,
            query=query,
            tools_used=plan,
            status="Success"
        )

        return report