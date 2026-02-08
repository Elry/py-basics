from abc import ABC, abstractmethod

class BaseIngestor(ABC):
    @abstractmethod
    def auth(self):
        """Handle login/auth logic."""
        pass

    @abstractmethod
    def load_data(self, source: str) -> list[str]:
        """Must return a list of text chunks."""
        pass

class JiraIngestor(BaseIngestor):
    def auth(self):
        print("Authenticating with Atlassian API Token...")

    def load_data(self, source: str):
        self.auth()
        return [f"Ticket {source}: Bug in login", "Ticket 42: Fix CSS"]

class PDFIngestor(BaseIngestor):
    def auth(self):
        print("Checking file permissions...")

    def load_data(self, source: str):
        self.auth()
        return [f"Page 1 of {source} content...", "Page 2 content..."]

# Factory (Dynamic switch)
def get_ingestor(source_type: str) -> BaseIngestor:
    ingestors = {
            "jira": JiraIngestor(),
            "pdf": PDFIngestor()
    }
    return ingestors.get(source_type)

ingestor = get_ingestor("jira")
data = ingestor.load_data("CPQ-7072")
print(data)
