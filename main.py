import os
import subprocess
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


# ================================
# 🔹 EMBEDDING MODEL
# ================================
model = SentenceTransformer('all-MiniLM-L6-v2')


# ================================
# 🔹 STEP 1: LOAD CODE FILES
# ================================
def load_code(folder):
    texts = []
    file_names = []

    for file in os.listdir(folder):
        if not file.endswith(".py"):
            continue

        with open(os.path.join(folder, file), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

            # Split by functions
            chunks = content.split("def ")

            for chunk in chunks:
                if chunk.strip() == "":
                    continue

                chunk = "def " + chunk if not chunk.startswith("def") else chunk

                texts.append(chunk)
                file_names.append(file)

    return texts, file_names


# ================================
# 🔹 STEP 2: EMBEDDINGS
# ================================
def embed_texts(texts):
    embeddings = model.encode(texts)

    embeddings = np.array(embeddings).astype("float32")

    # FAISS index create
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index


# ================================
# 🔹 STEP 3: CREATE INDEX
# ================================
def create_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))
    return index


# ================================
# 🔹 STEP 4: SEARCH
# ================================
def search(query, texts, file_names, index):
    query_vec = model.encode([query]).astype("float32")

    D, I = index.search(query_vec, k=3)

    results = []
    for i in I[0]:
        results.append((texts[i], file_names[i]))

    return results


# ================================
# 🔹 STEP 5: GENERATE ANSWER (OLLAMA)
# ================================
def generate_answer(query, results):
    context = ""

    for res, file in results:
        context += f"\nFile: {file}\n{res}\n"

    context = context[:2000]

    prompt = f"""
You are a code assistant.

User question:
{query}

Relevant code:
{context}

Explain clearly.
"""

    # ✅ SAME indentation (inside function)
    import subprocess

    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=prompt.encode('utf-8'),
        capture_output=True
    )

    output = result.stdout.decode('utf-8', errors='ignore')

    return output



# ================================
# 🔹 MAIN EXECUTION
# ================================
if __name__ == "__main__":

    print("🔄 Loading codebase...")
    texts, file_names = load_code("my_project")

    print("🔄 Creating embeddings...")
    vectors = embed_texts(texts)

    print("🔄 Building index...")
    index = create_index(vectors)

    print("✅ Ready! Ask your questions.\n")

    while True:
        query = input("💬 Ask your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        print("\n🔍 Searching...\n")
        results = search(query, index, texts, file_names)

        print("📂 Top Matches:")
        for res, file in results:
            print(f"\n📄 File: {file}")
            print("🔎 Preview:\n", "\n".join(res.split("\n")[:5]))

        print("\n🤖 Generating AI answer...\n")
        answer = generate_answer(query, results)

        print("\n🔥 AI RESPONSE:\n")
        print(answer)
        print("\n" + "="*50 + "\n")
         

