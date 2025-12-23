# поки заготовка – далі доповнимо
class Writer:
    @staticmethod
    def suggest_branches(desc: str) -> int:
        tokens = len(desc.split())
        return 8 if tokens > 300 else (5 if tokens > 120 else 3)
