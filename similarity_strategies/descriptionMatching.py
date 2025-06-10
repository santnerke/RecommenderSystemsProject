from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

description = [
    "Ein junger Archäologe entdeckt eine alte Stadt tief im Dschungel. Als er die Stadt erforscht, entdeckt er ein mächtiges Artefakt, das ihn in eine gefährliche Abenteuerreise entführt. Mit Hilfe seiner Freunde muss er das Artefakt vor den falschen Händen schützen und die Geheimnisse der alten Stadt entschlüsseln.",
    "In einer dystopischen Zukunft lebt die Menschheit in einer riesigen Stadt, die von einer tyrannischen Regierung kontrolliert wird. Ein junger Rebellenführer entdeckt ein Geheimnis, das die Regierung umstürzen könnte, und muss sich auf eine gefährliche Mission begeben, um die Wahrheit ans Licht zu bringen.",
    "Ein Detektiv wird von einer reichen Familie beauftragt, den Mord an ihrem Sohn aufzuklären. Als er in die Ermittlungen eintaucht, entdeckt er ein komplexes Netzwerk von Lügen und Intrigen, das ihn zu einem unerwarteten Täter führt.",
    "Ein junger Mann entdeckt, dass er die Fähigkeit hat, durch die Zeit zu reisen. Als er in die Vergangenheit reist, um seine Familie zu retten, muss er sich mit den Konsequenzen seiner Handlungen auseinandersetzen und die Zeitlinie wiederherstellen.",
    "Ein Team von Wissenschaftlern entdeckt ein neues Leben auf einem fernen Planeten. Als sie die neue Spezies erforschen, entdecken sie, dass sie eine Bedrohung für die Menschheit darstellt und müssen sich entscheiden, ob sie die neue Spezies retten oder vernichten sollen.",
    "Ein junger Boxer wird von einem erfahrenen Trainer entdeckt und zu einem Champion ausgebildet. Als er den Höhepunkt seiner Karriere erreicht, muss er sich mit den Konsequenzen seines Erfolgs auseinandersetzen und entscheiden, ob er seine Karriere fortsetzen oder sich zurückziehen soll.",
    "Ein Team von Freunden entdeckt ein altes, verlassenes Haus, das von einem Fluch heimgesucht wird. Als sie das Haus erforschen, entdecken sie, dass der Fluch real ist und müssen sich entscheiden, ob sie das Haus verlassen oder den Fluch brechen sollen.",
    "Ein junger Mann entdeckt, dass er die Fähigkeit hat, die Gedanken anderer Menschen zu lesen. Als er diese Fähigkeit nutzt, um Verbrechen aufzuklären, muss er sich mit den Konsequenzen seiner Handlungen auseinandersetzen und entscheiden, ob er seine Fähigkeit nutzen oder verbergen soll."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(description)

similarity_matrix = cosine_similarity(tfidf_matrix)

idx = 0
similarities = similarity_matrix[idx]

similarities[idx] = -1
most_similar_idx = np.argsort(similarities)[::-1][:5]

print("Original:", description[idx])
for film in most_similar_idx:
    print("Ähnlichste Filme:", description[film])
