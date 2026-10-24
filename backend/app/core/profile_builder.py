class ProfileBuilder:

    @staticmethod
    def build(memories):

        interests = set()
        projects = set()

        for memory in memories:

            text = memory.content.lower()

            if "python" in text:
                interests.add("Python")

            if "ai" in text:
                interests.add("AI")

            if "minni" in text:
                projects.add("Minni")

        return {
            "interests": sorted(
                list(interests)
            ),
            "projects": sorted(
                list(projects)
            )
        }

