from ollama import chat
print("Well-come to my QuestionBank Mind")
system_msg="You are from singer.Answer accordingly.Answer in one sentence"
history=[
    {
        "role":"system",
        "content":system_msg
    }
]
while True:
    question= input("You:")
    if question== "":
        print("AI Reddy☠️:Nuv em type cheyyaleveee......🤦‍♂️")
        continue
    if question.lower().strip()=='exit' or question.lower().strip()=='bye':
        print("Thankyou!Get lost....😁😁")
        break
    if question.lower().strip()=="/history":
        print("--------Your conversation so far------")
        if len(history)<2:
            print("Nothing here so far....")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="You"
            else:
                speaker="AI Reddy"
            print(f"{speaker}:{msg['content']}")
        print("--------------------------------------")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("Your chat history has been cleared.Start a fresh conversation")
        print()
        continue
    history.append({"role":"user","content":question})
    try:
        response=chat(
            model="llama3.2",
            messages=history
        )
        reply=response["message"]["content"]
        history.append({"role":"assistant","content":reply})
        print(f"AI Reddy☠️:{reply}")
        print()
    except Exception as e:
        print("Unknown issue,Is ollama running?")
