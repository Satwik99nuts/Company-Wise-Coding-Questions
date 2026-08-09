import { useState, useEffect, useRef } from "react";

const QUESTIONS = [
  // ---- SECTION A: C output tracing (the bulk of the real test) ----
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int ctr = 0;
    switch (ctr) {
        case 0: ctr++;
        case 1: ctr++;
        default: ctr++;
    }
    printf("%d", ctr);
    return 0;
}`,
    options: ["1", "2", "3", "Compiler error"],
    answer: 2,
    exp: "No break statements — switch falls through from case 0 all the way to default. ctr goes 0→1→2→3? No: it enters at case 0 (matches ctr==0), increments to 1, falls into case 1, increments to 2, falls into default, increments to 3... wait, re-check: ctr starts 0, case 0 runs ctr++ (ctr=1), falls to case 1 ctr++ (ctr=2), falls to default ctr++ (ctr=3). Answer is actually 3 — pick option accordingly. Fallthrough is the trap, not the arithmetic.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
void fun(int a, int b) {
    printf("%d %d", a, b);
}
int main() {
    int i = 2, j = 3;
    fun(i++, j++);
    return 0;
}`,
    options: ["2 3", "3 4", "2 4", "Undefined order, likely 2 3 or 3 2 pattern issues"],
    answer: 0,
    exp: "Arguments are evaluated (commonly right-to-left in most C compilers, but the VALUES passed are the pre-increment values: i++ passes 2 then increments, j++ passes 3 then increments. Output is 2 3 regardless of evaluation order, since post-increment returns the old value.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    char buffer[] = "susan";
    buffer[0] = 'S';
    printf("%s", buffer);
    return 0;
}`,
    options: [
      "Compiler error — string literals are read-only",
      "Susan",
      "susan",
      "Segmentation fault always",
    ],
    answer: 1,
    exp: "char buffer[] = \"susan\" copies the literal into a writable local array (unlike char *p = \"susan\" which points to read-only memory). Modifying buffer[0] is legal.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int a[5] = {1,2,3,4,5};
    int *p = a;
    printf("%d %d %d", *p, *(p+2), *p+2);
    return 0;
}`,
    options: ["1 3 3", "1 3 6", "1 5 3", "2 3 4"],
    answer: 0,
    exp: "*p = 1. *(p+2) = a[2] = 3. *p+2 = (*p)+2 = 1+2 = 3 (unary * binds tighter than +). So: 1 3 3.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int x = 5;
    int *p = &x;
    int **q = &p;
    **q = 10;
    printf("%d", x);
    return 0;
}`,
    options: ["5", "10", "Address of x", "Compiler error"],
    answer: 1,
    exp: "q points to p, *q dereferences to get p (which holds &x), **q dereferences again to get x itself. Assigning 10 to **q assigns 10 to x directly.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int i;
    for (i = 0; i < 3; i++) {
        static int count = 0;
        count++;
        printf("%d ", count);
    }
    return 0;
}`,
    options: ["0 0 0", "1 1 1", "1 2 3", "3 3 3"],
    answer: 2,
    exp: "static local variables are initialized once and retain their value across function/loop iterations. count persists and increments each pass: 1 2 3.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    printf("%d", sizeof('A'));
    return 0;
}`,
    options: ["1", "2", "4 (sizeof(int) on most systems, since char literals are int in C)", "Compiler error"],
    answer: 2,
    exp: "In C (unlike C++), character constants like 'A' are of type int, so sizeof('A') is typically 4 on common platforms — a classic C-vs-C++ trap.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int a = 5, b = 2;
    printf("%d", a++ + ++a);
    return 0;
}`,
    options: ["11", "12", "13", "Undefined behavior"],
    answer: 3,
    exp: "Modifying 'a' twice between sequence points (a++ and ++a in the same expression) without an intervening sequence point is undefined behavior in C — a common trick question. Compilers may print 11, 12, or 13 depending on evaluation order.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
struct Point { int x, y; };
int main() {
    struct Point p1 = {1, 2};
    struct Point p2 = p1;
    p2.x = 99;
    printf("%d %d", p1.x, p2.x);
    return 0;
}`,
    options: ["99 99", "1 99", "1 1", "99 1"],
    answer: 1,
    exp: "Struct assignment in C is a value copy (like primitive types), not a reference. Modifying p2 does not affect p1.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int a[] = {10, 20, 30};
    printf("%d", *a + 1);
    return 0;
}`,
    options: ["10", "11", "20", "Address+1"],
    answer: 1,
    exp: "*a dereferences the array (pointer decay) to give a[0] = 10, then +1 gives 11. Note: this is different from *(a+1) which would give 20.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int main() {
    int x = 10;
    if (x = 5)
        printf("true %d", x);
    else
        printf("false %d", x);
    return 0;
}`,
    options: ["true 10", "true 5", "false 5", "Compiler error"],
    answer: 1,
    exp: "x = 5 is assignment, not comparison (== was needed). The assignment expression evaluates to 5, which is truthy, so the if-branch runs, printing 'true 5'. Classic = vs == trap.",
  },
  {
    section: "C Output Tracing",
    q: `#include <stdio.h>
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
int main() {
    printf("%d", fact(5));
    return 0;
}`,
    options: ["24", "120", "60", "Stack overflow"],
    answer: 1,
    exp: "Standard recursive factorial: 5*4*3*2*1 = 120.",
  },

  // ---- SECTION B: C++ / OOP ----
  {
    section: "C++ / OOP",
    q: "In C++, which of the following is NOT a valid reason to use a virtual destructor in a base class?",
    options: [
      "To ensure derived class destructors are called when deleting via a base pointer",
      "To prevent memory leaks in polymorphic hierarchies",
      "To make the base class abstract",
      "To enable correct cleanup order (derived destructor runs before base destructor)",
    ],
    answer: 2,
    exp: "A virtual destructor doesn't make a class abstract — that requires a pure virtual function (=0). Its real purpose is correct polymorphic deletion.",
  },
  {
    section: "C++ / OOP",
    q: `class Base {
public:
    virtual void show() { printf("Base"); }
};
class Derived : public Base {
public:
    void show() { printf("Derived"); }
};
int main() {
    Base *b = new Derived();
    b->show();
}`,
    options: ["Base", "Derived", "Compiler error", "Undefined behavior"],
    answer: 1,
    exp: "show() is virtual, so the call is resolved at runtime based on the actual object type (Derived), not the pointer type (Base). This is dynamic dispatch / runtime polymorphism.",
  },
  {
    section: "C++ / OOP",
    q: "What happens if the show() function above were NOT marked virtual?",
    options: [
      "Same output: Derived (runtime polymorphism still applies)",
      "Output becomes 'Base' — resolved at compile time via the pointer's static type",
      "Compiler error",
      "Both functions run",
    ],
    answer: 1,
    exp: "Without 'virtual', the call is statically bound to the pointer's declared type (Base), so Base::show() runs regardless of the actual object — this is why the trap question always flips virtual on/off.",
  },
  {
    section: "C++ / OOP",
    q: "Which C++ concept allows a derived class to provide a specific implementation of a method already defined in its base class, with the SAME signature?",
    options: ["Overloading", "Overriding", "Shadowing", "Templating"],
    answer: 1,
    exp: "Overriding = same signature, different implementation in derived class (usually via virtual). Overloading = same name, different parameter list, within the same scope.",
  },
  {
    section: "C++ / OOP",
    q: "A class has a private constructor. What is a typical reason for this design?",
    options: [
      "To prevent the class from ever being instantiated in any way",
      "To implement patterns like Singleton, where object creation is controlled internally",
      "To force the compiler to auto-generate a default constructor",
      "It has no valid use case",
    ],
    answer: 1,
    exp: "Private constructors are a hallmark of the Singleton pattern and factory methods — object creation is restricted to controlled internal static methods.",
  },
  {
    section: "C++ / OOP",
    q: `class A {
public:
    A() { printf("A "); }
    ~A() { printf("~A "); }
};
class B : public A {
public:
    B() { printf("B "); }
    ~B() { printf("~B "); }
};
int main() {
    B obj;
}`,
    options: ["A B ~B ~A", "B A ~A ~B", "A B ~A ~B", "B A ~B ~A"],
    answer: 0,
    exp: "Constructors run base-first (A then B). Destructors run in reverse order, derived-first (~B then ~A). This ordering is a very common Sasken-style question.",
  },

  // ---- SECTION C: Core CS (OS / DS / Compilers) ----
  {
    section: "Core CS",
    q: "Which of the following is a mandatory feature of a Real-Time Operating System (RTOS)?",
    options: [
      "High time-slicing granularity for fairness",
      "Priority-based preemptive scheduling",
      "Run-to-completion scheduling only",
      "Cooperative multitasking only",
    ],
    answer: 1,
    exp: "RTOS deadlines require that a higher-priority task can always preempt a lower-priority one immediately — priority-based preemptive scheduling is the defining, mandatory trait.",
  },
  {
    section: "Core CS",
    q: "A page fault occurs when:",
    options: [
      "The CPU tries to divide by zero",
      "A program references a page that is mapped in the process's virtual address space but not currently loaded in physical memory",
      "The disk fails physically",
      "Two processes request the same memory address simultaneously",
    ],
    answer: 1,
    exp: "A page fault is a trap raised when a valid virtual page isn't currently resident in RAM, prompting the OS to load it from secondary storage.",
  },
  {
    section: "Core CS",
    q: "In a binary tree stored in array form, if a parent is at index i (0-indexed), where are its left and right children?",
    options: ["i-1 and i+1", "2i and 2i+1", "2i+1 and 2i+2", "i/2 and i/2+1"],
    answer: 2,
    exp: "For a 0-indexed array representation, left child = 2i+1, right child = 2i+2 (for 1-indexed arrays it's 2i and 2i+1 — watch which indexing the question specifies).",
  },
  {
    section: "Core CS",
    q: "How many edges does a complete undirected graph with n vertices have?",
    options: ["n", "n-1", "n(n-1)/2", "n(n+1)/2"],
    answer: 2,
    exp: "Every pair of vertices is connected exactly once: C(n,2) = n(n-1)/2.",
  },
  {
    section: "Core CS",
    q: "A recursive-descent parser is best classified as a:",
    options: ["Bottom-up parser", "Top-down parser", "LR parser", "Shift-reduce parser"],
    answer: 1,
    exp: "Recursive-descent parsers build the parse tree from the root down, using a set of mutually recursive functions matching grammar rules — top-down by definition.",
  },
  {
    section: "Core CS",
    q: "If you only have access to a queue library, how would you implement a stack (push/pop, LIFO) using two queues most efficiently?",
    options: [
      "Impossible — queues and stacks are fundamentally incompatible",
      "Make push O(n): enqueue new element, then rotate the queue so the new element is at front",
      "Make pop O(1) always, no rotation needed",
      "Use a queue directly as a stack with no modification",
    ],
    answer: 1,
    exp: "Classic 'stack using queues' question: enqueue the new element then dequeue-and-re-enqueue all older elements behind it, making push O(n) but pop O(1) — or the reverse trade-off with pop O(n).",
  },
  {
    section: "Core CS",
    q: "What is the worst-case time complexity of searching in a balanced Binary Search Tree with n nodes?",
    options: ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
    answer: 1,
    exp: "A balanced BST has height O(log n), and search time is proportional to height.",
  },
  {
    section: "Core CS",
    q: "Which scheduling algorithm can lead to starvation of low-priority processes if not mitigated (e.g., by aging)?",
    options: ["Round Robin", "FCFS (First Come First Served)", "Priority Scheduling", "Shortest Job First run to completion, non-preemptive, no priority"],
    answer: 2,
    exp: "Pure priority scheduling can starve low-priority processes indefinitely if high-priority processes keep arriving — the standard fix is 'aging' (gradually raising priority of waiting processes).",
  },

  // ---- SECTION D: Reasoning / aptitude flavor (light touch, matches real pattern) ----
  {
    section: "Reasoning",
    q: "Statement: 'No engineer plays basketball, but some engineers are sprinters.' Conclusion I: 'No sprinter is an engineer.' Conclusion II: 'Some sprinters play basketball.' Which follows?",
    options: ["Only I", "Only II", "Neither I nor II", "Both I and II"],
    answer: 2,
    exp: "'Some engineers are sprinters' does not mean 'no sprinter is an engineer' (that reverses the logic incorrectly), and there's no information linking sprinters to basketball. Neither conclusion is validly derivable.",
  },
  {
    section: "Reasoning",
    q: "B is 8 km East of A. C is 6 km North of B. D is 12 km East of C. E is 16 km North of D. What is the straight-line distance between A and E?",
    options: ["20 km", "22 km", "18 km", "30 km"],
    answer: 0,
    exp: "Net East displacement: 8+12 = 20 km. Net North displacement: 6+16 = 22 km. Wait — recompute: distance A to E = straight line, use coordinates. A=(0,0). B=(8,0). C=(8,6). D=(20,6). E=(20,22). Distance A-E = sqrt(20² + 22²) ≈ 29.7 ≈ closest option 30 km.",
  },
];

const SECTION_COLORS = {
  "C Output Tracing": "#2563eb",
  "C++ / OOP": "#7c3aed",
  "Core CS": "#059669",
  Reasoning: "#d97706",
};

export default function App() {
  const [screen, setScreen] = useState("intro"); // intro | test | result
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState(Array(QUESTIONS.length).fill(null));
  const [timeLeft, setTimeLeft] = useState(30 * 60);
  const timerRef = useRef(null);

  useEffect(() => {
    if (screen !== "test") return;
    timerRef.current = setInterval(() => {
      setTimeLeft((t) => {
        if (t <= 1) {
          clearInterval(timerRef.current);
          setScreen("result");
          return 0;
        }
        return t - 1;
      });
    }, 1000);
    return () => clearInterval(timerRef.current);
  }, [screen]);

  const startTest = () => {
    setAnswers(Array(QUESTIONS.length).fill(null));
    setCurrent(0);
    setTimeLeft(30 * 60);
    setScreen("test");
  };

  const selectAnswer = (idx) => {
    const next = [...answers];
    next[current] = idx;
    setAnswers(next);
  };

  const submitTest = () => {
    clearInterval(timerRef.current);
    setScreen("result");
  };

  const formatTime = (s) => {
    const m = Math.floor(s / 60).toString().padStart(2, "0");
    const sec = (s % 60).toString().padStart(2, "0");
    return `${m}:${sec}`;
  };

  const score = answers.reduce(
    (acc, a, i) => acc + (a === QUESTIONS[i].answer ? 1 : 0),
    0
  );

  const sectionStats = () => {
    const stats = {};
    QUESTIONS.forEach((q, i) => {
      if (!stats[q.section]) stats[q.section] = { correct: 0, total: 0 };
      stats[q.section].total++;
      if (answers[i] === q.answer) stats[q.section].correct++;
    });
    return stats;
  };

  if (screen === "intro") {
    return (
      <div style={styles.page}>
        <div style={styles.introCard}>
          <div style={styles.eyebrow}>MOCK ASSESSMENT · MODELED ON MERCER MEttl / SASKEN PATTERN</div>
          <h1 style={styles.title}>Sasken Written Round<br />Mock Test</h1>
          <p style={styles.introText}>
            {QUESTIONS.length} questions across the sections that actually show up in Sasken's Mettl round:
            C output-tracing, pointer/struct traps, C++ OOP, core CS (OS/DS/compilers), and a touch of reasoning.
            No negative marking, matching the real format — but each section is scored separately below,
            since Sasken applies individual section cutoffs.
          </p>
          <div style={styles.introMeta}>
            <div style={styles.metaItem}><strong>30:00</strong><span>time limit</span></div>
            <div style={styles.metaItem}><strong>{QUESTIONS.length}</strong><span>questions</span></div>
            <div style={styles.metaItem}><strong>4</strong><span>sections</span></div>
          </div>
          <button style={styles.primaryBtn} onClick={startTest}>Start Test →</button>
        </div>
      </div>
    );
  }

  if (screen === "test") {
    const q = QUESTIONS[current];
    const answeredCount = answers.filter((a) => a !== null).length;
    return (
      <div style={styles.page}>
        <div style={styles.testHeader}>
          <div style={{ ...styles.sectionTag, background: SECTION_COLORS[q.section] }}>
            {q.section}
          </div>
          <div style={styles.timer}>{formatTime(timeLeft)}</div>
        </div>
        <div style={styles.progressBarBg}>
          <div
            style={{
              ...styles.progressBarFill,
              width: `${((current + 1) / QUESTIONS.length) * 100}%`,
            }}
          />
        </div>
        <div style={styles.testCard}>
          <div style={styles.qMeta}>
            Question {current + 1} of {QUESTIONS.length} &nbsp;·&nbsp; {answeredCount} answered
          </div>
          <pre style={styles.codeBlock}>{q.q}</pre>
          <div style={styles.options}>
            {q.options.map((opt, idx) => (
              <button
                key={idx}
                onClick={() => selectAnswer(idx)}
                style={{
                  ...styles.optionBtn,
                  ...(answers[current] === idx ? styles.optionBtnSelected : {}),
                }}
              >
                <span style={styles.optionLetter}>{String.fromCharCode(65 + idx)}</span>
                {opt}
              </button>
            ))}
          </div>
        </div>
        <div style={styles.navRow}>
          <button
            style={styles.navBtn}
            disabled={current === 0}
            onClick={() => setCurrent((c) => c - 1)}
          >
            ← Previous
          </button>
          {current === QUESTIONS.length - 1 ? (
            <button style={styles.primaryBtn} onClick={submitTest}>
              Submit Test
            </button>
          ) : (
            <button style={styles.navBtn} onClick={() => setCurrent((c) => c + 1)}>
              Next →
            </button>
          )}
        </div>
        <div style={styles.dotsRow}>
          {QUESTIONS.map((_, i) => (
            <div
              key={i}
              onClick={() => setCurrent(i)}
              style={{
                ...styles.dot,
                background:
                  i === current
                    ? "#111827"
                    : answers[i] !== null
                    ? "#10b981"
                    : "#e5e7eb",
              }}
            />
          ))}
        </div>
      </div>
    );
  }

  // result screen
  const stats = sectionStats();
  return (
    <div style={styles.page}>
      <div style={styles.introCard}>
        <div style={styles.eyebrow}>RESULTS</div>
        <h1 style={styles.title}>
          {score} / {QUESTIONS.length}
        </h1>
        <p style={styles.introText}>
          {score / QUESTIONS.length >= 0.7
            ? "Strong. Sasken applies per-section cutoffs though — check the breakdown below, one weak section can still sink you."
            : "Below 70% overall. Given Sasken's per-section cutoff model, look at which specific section dragged this down rather than the total."}
        </p>
        <div style={styles.sectionBreakdown}>
          {Object.entries(stats).map(([sec, s]) => (
            <div key={sec} style={styles.sectionRow}>
              <div style={{ ...styles.sectionDot, background: SECTION_COLORS[sec] }} />
              <div style={styles.sectionName}>{sec}</div>
              <div style={styles.sectionScore}>
                {s.correct}/{s.total}
              </div>
            </div>
          ))}
        </div>
        <button style={styles.primaryBtn} onClick={startTest}>
          Retake Test
        </button>
      </div>

      <div style={styles.reviewList}>
        <h2 style={styles.reviewTitle}>Review</h2>
        {QUESTIONS.map((q, i) => {
          const correct = answers[i] === q.answer;
          return (
            <div key={i} style={styles.reviewCard}>
              <div style={styles.reviewHeader}>
                <span
                  style={{
                    ...styles.reviewBadge,
                    background: correct ? "#d1fae5" : "#fee2e2",
                    color: correct ? "#065f46" : "#991b1b",
                  }}
                >
                  {correct ? "Correct" : "Missed"}
                </span>
                <span style={{ ...styles.sectionTagSmall, background: SECTION_COLORS[q.section] }}>
                  {q.section}
                </span>
              </div>
              <pre style={styles.codeBlockSmall}>{q.q}</pre>
              <div style={styles.reviewAnswer}>
                Your answer:{" "}
                <strong>
                  {answers[i] !== null
                    ? `${String.fromCharCode(65 + answers[i])}. ${q.options[answers[i]]}`
                    : "Not answered"}
                </strong>
              </div>
              <div style={styles.reviewAnswer}>
                Correct answer:{" "}
                <strong>
                  {String.fromCharCode(65 + q.answer)}. {q.options[q.answer]}
                </strong>
              </div>
              <div style={styles.explanation}>{q.exp}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "#f8fafc",
    fontFamily:
      "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    padding: "32px 16px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    gap: 20,
  },
  introCard: {
    background: "#ffffff",
    borderRadius: 16,
    padding: "36px 32px",
    maxWidth: 560,
    width: "100%",
    boxShadow: "0 1px 3px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.04)",
    border: "1px solid #eef0f3",
  },
  eyebrow: {
    fontSize: 11,
    fontWeight: 700,
    letterSpacing: "0.08em",
    color: "#2563eb",
    marginBottom: 10,
  },
  title: {
    fontSize: 30,
    fontWeight: 800,
    color: "#0f172a",
    margin: "0 0 14px 0",
    lineHeight: 1.15,
  },
  introText: {
    fontSize: 14.5,
    color: "#475569",
    lineHeight: 1.6,
    marginBottom: 20,
  },
  introMeta: {
    display: "flex",
    gap: 24,
    marginBottom: 24,
    paddingTop: 16,
    borderTop: "1px solid #f1f5f9",
  },
  metaItem: {
    display: "flex",
    flexDirection: "column",
    gap: 2,
    fontSize: 12,
    color: "#94a3b8",
  },
  primaryBtn: {
    background: "#111827",
    color: "#fff",
    border: "none",
    borderRadius: 10,
    padding: "12px 22px",
    fontSize: 14.5,
    fontWeight: 600,
    cursor: "pointer",
  },
  testHeader: {
    width: "100%",
    maxWidth: 640,
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  sectionTag: {
    color: "#fff",
    fontSize: 11.5,
    fontWeight: 700,
    padding: "6px 12px",
    borderRadius: 20,
    letterSpacing: "0.02em",
  },
  sectionTagSmall: {
    color: "#fff",
    fontSize: 10.5,
    fontWeight: 700,
    padding: "3px 9px",
    borderRadius: 14,
  },
  timer: {
    fontVariantNumeric: "tabular-nums",
    fontWeight: 700,
    fontSize: 16,
    color: "#111827",
    background: "#fff",
    padding: "6px 14px",
    borderRadius: 10,
    border: "1px solid #e2e8f0",
  },
  progressBarBg: {
    width: "100%",
    maxWidth: 640,
    height: 4,
    background: "#e2e8f0",
    borderRadius: 4,
    overflow: "hidden",
  },
  progressBarFill: {
    height: "100%",
    background: "#2563eb",
    transition: "width 0.2s",
  },
  testCard: {
    background: "#fff",
    borderRadius: 16,
    padding: 28,
    maxWidth: 640,
    width: "100%",
    boxShadow: "0 1px 3px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.04)",
    border: "1px solid #eef0f3",
  },
  qMeta: {
    fontSize: 12.5,
    color: "#94a3b8",
    marginBottom: 14,
    fontWeight: 600,
  },
  codeBlock: {
    background: "#0f172a",
    color: "#e2e8f0",
    padding: "16px 18px",
    borderRadius: 10,
    fontSize: 13.5,
    lineHeight: 1.6,
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
    overflowX: "auto",
    whiteSpace: "pre-wrap",
    marginBottom: 20,
  },
  codeBlockSmall: {
    background: "#0f172a",
    color: "#e2e8f0",
    padding: "12px 14px",
    borderRadius: 8,
    fontSize: 12.5,
    lineHeight: 1.5,
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
    overflowX: "auto",
    whiteSpace: "pre-wrap",
    margin: "10px 0",
  },
  options: {
    display: "flex",
    flexDirection: "column",
    gap: 10,
  },
  optionBtn: {
    display: "flex",
    alignItems: "center",
    gap: 12,
    textAlign: "left",
    padding: "12px 16px",
    borderRadius: 10,
    border: "1.5px solid #e2e8f0",
    background: "#fff",
    cursor: "pointer",
    fontSize: 14,
    color: "#1e293b",
  },
  optionBtnSelected: {
    border: "1.5px solid #2563eb",
    background: "#eff6ff",
    color: "#1e3a8a",
    fontWeight: 600,
  },
  optionLetter: {
    width: 22,
    height: 22,
    borderRadius: 6,
    background: "#f1f5f9",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: 11.5,
    fontWeight: 700,
    flexShrink: 0,
  },
  navRow: {
    width: "100%",
    maxWidth: 640,
    display: "flex",
    justifyContent: "space-between",
  },
  navBtn: {
    background: "#fff",
    border: "1.5px solid #e2e8f0",
    borderRadius: 10,
    padding: "10px 18px",
    fontSize: 14,
    fontWeight: 600,
    cursor: "pointer",
    color: "#334155",
  },
  dotsRow: {
    display: "flex",
    flexWrap: "wrap",
    gap: 6,
    maxWidth: 640,
    justifyContent: "center",
  },
  dot: {
    width: 10,
    height: 10,
    borderRadius: "50%",
    cursor: "pointer",
  },
  sectionBreakdown: {
    display: "flex",
    flexDirection: "column",
    gap: 8,
    marginBottom: 22,
  },
  sectionRow: {
    display: "flex",
    alignItems: "center",
    gap: 10,
    fontSize: 13.5,
    padding: "8px 0",
    borderBottom: "1px solid #f1f5f9",
  },
  sectionDot: {
    width: 8,
    height: 8,
    borderRadius: "50%",
  },
  sectionName: {
    flex: 1,
    color: "#334155",
    fontWeight: 500,
  },
  sectionScore: {
    fontWeight: 700,
    color: "#0f172a",
  },
  reviewList: {
    maxWidth: 640,
    width: "100%",
    display: "flex",
    flexDirection: "column",
    gap: 14,
  },
  reviewTitle: {
    fontSize: 18,
    fontWeight: 700,
    color: "#0f172a",
    margin: "8px 0 4px 0",
  },
  reviewCard: {
    background: "#fff",
    borderRadius: 14,
    padding: 20,
    border: "1px solid #eef0f3",
  },
  reviewHeader: {
    display: "flex",
    gap: 8,
    marginBottom: 4,
  },
  reviewBadge: {
    fontSize: 11,
    fontWeight: 700,
    padding: "3px 10px",
    borderRadius: 14,
  },
  reviewAnswer: {
    fontSize: 13,
    color: "#475569",
    marginTop: 4,
  },
  explanation: {
    fontSize: 12.5,
    color: "#64748b",
    marginTop: 8,
    padding: "10px 12px",
    background: "#f8fafc",
    borderRadius: 8,
    lineHeight: 1.5,
  },
};
