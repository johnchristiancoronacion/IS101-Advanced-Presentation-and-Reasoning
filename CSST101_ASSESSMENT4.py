def reason_about_member(name: str, is_member: bool, extra_info: str | None = None):
    steps = []
    steps.append(f"1) Input: person = '{name}'")
    steps.append("2) Rule: If a person is a library member, assume they can borrow books.")

    if not is_member:
        steps.append("3) Fact: The person is NOT a library member.")
        steps.append("4) Conclusion: The rule does not apply → cannot borrow books.")
        return steps

    # Apply default rule
    steps.append("3) Fact: The person IS a library member.")
    steps.append("4) Default conclusion: the person can borrow books.")
    conclusion = "can borrow books"

    # New information check
    if extra_info:
        steps.append(f"5) New information provided: {extra_info}")
        info = extra_info.lower()

        if "unpaid fine" in info or "overdue" in info:
            steps.append("6) This new information contradicts the default rule.")
            steps.append("7) Retracting default conclusion.")
            conclusion = "cannot borrow books"
            steps.append(f"8) Revised conclusion: the person {conclusion}.")
            return steps

        steps.append("6) The new information does not contradict the default rule.")

    steps.append(f"7) Final conclusion: the person {conclusion}.")
    return steps


def interactive():
    print("=== Library Borrowing Reasoner ===")
    name = input("Enter person name: ").strip()
    member_ans = input("Is the person a library member? (y/n): ").strip().lower()
    is_member = member_ans.startswith('y')

    extra_info = None
    add_info = input("Add extra info? (e.g., 'has unpaid fine', 'overdue book') (y/n): ").strip().lower()
    if add_info.startswith('y'):
        extra_info = input("Type extra information: ").strip()

    steps = reason_about_member(name, is_member, extra_info)

    print("\n--- Reasoning trace ---")
    for step in steps:
        print(step)
    print("--- End of trace ---\n")


if __name__ == "__main__":
    while True:
        interactive()
        again = input("Try another person? (y/n): ").strip().lower()
        if not again.startswith('y'):
            print("Goodbye.")
            break
