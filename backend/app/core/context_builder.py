class ContextBuilder:

    @staticmethod
    def build(
        query,
        profile,
        memories
    ):

        lines = []

        lines.append(
            f"User Query: {query}"
        )

        lines.append("")

        lines.append("Interests:")

        for item in profile.get(
            "interests",
            []
        ):
            lines.append(
                f"- {item}"
            )

        lines.append("")

        lines.append("Projects:")

        for item in profile.get(
            "projects",
            []
        ):
            lines.append(
                f"- {item}"
            )

        lines.append("")

        lines.append(
            "Relevant Memories:"
        )

        for memory in memories:
            lines.append(
                f"- {memory['content']}"
            )

        return "\n".join(lines)
