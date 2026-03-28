import os
from flask import Flask, render_template, request
keyword_hints={
    "subarray":"Try sliding window or prefix sum approach",
    "palindrome": "Two pointers from both ends usually works",
    "cycle": "Slow and fast pointer technique might help",
    "sorted": "Binary search could be applicable",
    "bst": "Inorder traversal gives sorted order",
    "maximum": "Think about greedy or DP",
    "minimum": "Check greedy or binary search on answer",
    "window": "Try a fixed or variable sliding window",
    "sum": "Prefix sum or hashmap may help",
    "k consecutive": "Classic sliding window pattern",
    "range": "Prefix sum or difference array might work",
    "reverse": "Two pointers or in-place reversal",
    "anagram": "Frequency count using hashmap",
    "substring": "Sliding window is commonly used",
    "character": "Consider frequency array or hashmap",
    "graph": "Model problem as graph",
    "connected": "DFS or BFS traversal",
    "shortest": "BFS (unweighted) or Dijkstra",
    "cycle detection": "DFS with visited states",
    "topological": "Kahn's algorithm or DFS ordering",
    "dp": "Check overlapping subproblems and optimal substructure",
    "ways": "DP counting problem",
    "maximum sum": "DP or Kadane's algorithm",
    "minimum cost": "DP with state transition",
    "longest": "DP or two pointers depending on constraints",
    "next greater": "Use monotonic stack",
    "previous smaller": "Monotonic stack pattern",
    "parentheses": "Stack-based validation",
    "expression": "Stack for operators and operands",
    "search": "Check if binary search is possible",
    "peak": "Binary search on monotonic property",
    "tree": "Decide traversal strategy (DFS/BFS)",
    "depth": "DFS or BFS level order traversal",
    "height": "Recursive bottom-up approach",
    "ancestor": "Think about LCA logic"
    }

hints = {
    "array":{
        "approach":[
            "Try brute force first, then optimize",
            "Use two pointers or sliding window",
            "Think about prefix sums"
        ],
        "edge_cases":[
            "Empty array",
            "Single element",
            "All negative values",
            "Duplicates"
        ],
        "complexity":[
            "Try to find O(n) solution",
            "Avoid nested loops"
        ]
    },
    "linked_list":{
        "approach":[
            "Use slow-fast pointers",
            "Use dummy node technique",
            "Think about reversal logic"
        ],
        "edge_cases":[
            "Null head",
            "Single node",
            "Cycle in list"
        ],
        "complexity": [
            "One pass solution if possible",
            "O(1) extra space preferred"
        ]
    },
    "string": {
        "approach": [
            "Check if two pointers can be used",
            "Frequency count using hashmap",
            "Sliding window for substrings"
        ],
        "edge_cases": [
            "Empty string",
            "Single character",
            "All characters same"
        ],
        "complexity": [
            "Aim for O(n)",
            "Avoid repeated substring creation"
        ]
    },
    "tree": {
        "approach": [
            "Decide traversal: inorder, preorder, postorder",
            "Use recursion or stack",
            "Think top-down vs bottom-up"
        ],
        "edge_cases": [
            "Null root",
            "Single node tree",
            "Skewed tree"
        ],
        "complexity": [
            "Most traversals are O(n)",
            "Watch recursion stack space"
        ]
    }
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        problem=request.form["problem"].lower()
        category=request.form["category"]

        #keyword suggestions
        keyword_results =[] #for storing results
        printed =set()  #for avoiding duplictes(set)

        for word,hint in keyword_hints.items():
            if word in problem and hint not in printed:
                keyword_results.append(hint)
                printed.add(hint)

        if not keyword_results:
            keyword_results.append("No specific keywords found")

        #category suggestions
        category_data=hints.get(category)

        return render_template(
            "index.html",
            keyword_results=keyword_results,
            category_data=category_data
        )
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

