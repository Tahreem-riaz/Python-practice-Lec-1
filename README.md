<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Python - Lecture 01</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f5f7fa;
            color: #222;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            background-color: white;
            padding: 40px;
            border-radius: 12px;
        }

        h1 {
            text-align: center;
        }

        h2 {
            margin-top: 35px;
            border-bottom: 2px solid #ddd;
            padding-bottom: 8px;
        }

        h3 {
            margin-top: 25px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }

        th,
        td {
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #eee;
        }

        code {
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 4px;
        }

        pre {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .project {
            padding: 20px;
            background-color: #f7f7f7;
            border-left: 5px solid #555;
            margin-top: 15px;
        }
    </style>
</head>

<body>

<div class="container">

    <!-- ============================================ -->
    <!-- TITLE -->
    <!-- ============================================ -->

    <h1>🐍 Python — Lecture 01</h1>

    <h2>Python Fundamentals</h2>

    <p>
        This repository contains my practice work for
        <strong>Lecture 01 of my Python learning journey</strong>.
    </p>

    <p>
        The lecture focuses on the fundamental concepts needed
        to start writing basic Python programs, including
        variables, data types, operators, and type conversion.
    </p>


    <!-- ============================================ -->
    <!-- TOPICS -->
    <!-- ============================================ -->

    <h2>📚 Topics Covered</h2>

    <h3>1. Python Fundamentals</h3>

    <ul>
        <li>Python Character Set</li>
        <li>Variables</li>
        <li>Rules of Identifiers</li>
    </ul>


    <h3>2. Data Types</h3>

    <ul>
        <li>Integer (<code>int</code>)</li>
        <li>Floating Point (<code>float</code>)</li>
        <li>String (<code>str</code>)</li>
        <li>Boolean (<code>bool</code>)</li>
        <li>Complex (<code>complex</code>)</li>
        <li>Checking data types using <code>type()</code></li>
    </ul>


    <h3>3. Operators</h3>

    <ul>
        <li>Arithmetic Operators</li>
        <li>Comparison Operators</li>
        <li>Assignment Operators</li>
        <li>Logical Operators</li>
        <li>Membership Operators</li>
        <li>Identity Operators</li>
        <li>Bitwise Operators</li>
    </ul>


    <h3>4. Type Conversion &amp; Casting</h3>

    <ul>
        <li>Implicit Type Conversion</li>
        <li>Explicit Type Conversion</li>
        <li><code>int()</code></li>
        <li><code>float()</code></li>
        <li><code>str()</code></li>
        <li><code>bool()</code></li>
    </ul>


    <!-- ============================================ -->
    <!-- REPOSITORY STRUCTURE -->
    <!-- ============================================ -->

    <h2>📂 Repository Structure</h2>

    <pre>
lecture-01/
│
├── README.md
├── README.html
├── 01_fundamentals.py
├── 02_data_types.py
├── 03_operators.py
├── 04_type_conversion.py
└── 05_mini_project.py
    </pre>


    <!-- ============================================ -->
    <!-- FILE DESCRIPTION -->
    <!-- ============================================ -->

    <h2>📄 File Description</h2>

    <table>

        <thead>
            <tr>
                <th>File</th>
                <th>Description</th>
            </tr>
        </thead>

        <tbody>

            <tr>
                <td><code>01_fundamentals.py</code></td>
                <td>
                    Practice with character sets, variables,
                    and identifiers.
                </td>
            </tr>

            <tr>
                <td><code>02_data_types.py</code></td>
                <td>
                    Practice with Python's basic data types.
                </td>
            </tr>

            <tr>
                <td><code>03_operators.py</code></td>
                <td>
                    Practice with different types of operators.
                </td>
            </tr>

            <tr>
                <td><code>04_type_conversion.py</code></td>
                <td>
                    Practice with type conversion and casting.
                </td>
            </tr>

            <tr>
                <td><code>05_mini_project.py</code></td>
                <td>
                    A small project combining concepts from
                    the lecture.
                </td>
            </tr>

        </tbody>

    </table>


    <!-- ============================================ -->
    <!-- LEARNING GOALS -->
    <!-- ============================================ -->

    <h2>🎯 Learning Goals</h2>

    <p>
        By completing this lecture, I aim to understand how to:
    </p>

    <ul>
        <li>Create and use variables.</li>

        <li>Follow Python identifier rules.</li>

        <li>Recognize common Python data types.</li>

        <li>Check the type of a value.</li>

        <li>Perform operations using Python operators.</li>

        <li>Compare and manipulate values.</li>

        <li>Convert values between different data types.</li>

        <li>
            Combine these concepts to create simple Python programs.
        </li>
    </ul>


    <!-- ============================================ -->
    <!-- PRACTICE APPROACH -->
    <!-- ============================================ -->

    <h2>🛠️ Practice Approach</h2>

    <p>
        The programs in this lecture are designed for practice
        rather than simply memorizing syntax.
    </p>

    <p>
        My approach is:
    </p>

    <ol>
        <li>Understand the concept.</li>

        <li>Attempt the problem myself.</li>

        <li>Run and test the program.</li>

        <li>Experiment by changing values.</li>

        <li>
            Fix errors and understand why they occurred.
        </li>
    </ol>


    <!-- ============================================ -->
    <!-- MINI PROJECT -->
    <!-- ============================================ -->

    <h2>🚀 Mini Project</h2>

    <p>
        The final file combines the concepts learned throughout
        the lecture into a small practical Python program.
    </p>

    <div class="project">

        <h3>Personal Budget Calculator</h3>

        <p>
            <strong>File:</strong>
            <code>05_mini_project.py</code>
        </p>

        <p>
            The mini project uses the following concepts:
        </p>

        <ul>
            <li>Variables</li>
            <li>Data Types</li>
            <li>Arithmetic Operators</li>
            <li>Comparison Operators</li>
            <li>Logical Operators</li>
            <li>Type Conversion</li>
            <li>User Input</li>
        </ul>

        <p>
            The program calculates total expenses,
            remaining money, expense percentage,
            and budget status.
        </p>

    </div>


    <!-- ============================================ -->
    <!-- LEARNING PROGRESS -->
    <!-- ============================================ -->

    <h2>📈 Learning Progress</h2>

    <table>

        <thead>
            <tr>
                <th>Lecture</th>
                <th>Status</th>
            </tr>
        </thead>

        <tbody>

            <tr>
                <td>Lecture 01 — Python Fundamentals</td>
                <td>✅ Completed</td>
            </tr>

            <tr>
                <td>Lecture 02</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 03</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 04</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 05</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 06</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 07</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 08</td>
                <td>⬜ Not Started</td>
            </tr>

            <tr>
                <td>Lecture 09</td>
                <td>⬜ Not Started</td>
            </tr>

        </tbody>

    </table>


    <!-- ============================================ -->
    <!-- LANGUAGE -->
    <!-- ============================================ -->

    <h2>🐍 Language</h2>

    <p>
        <strong>Python 3</strong>
    </p>

    <p>
        This repository is part of my journey toward building
        a strong foundation in Python programming.
    </p>


    <!-- ============================================ -->
    <!-- TOPICS -->
    <!-- ============================================ -->

    <h2>🔖 Topics</h2>

    <p>
        <code>python</code>
        <code>python3</code>
        <code>programming</code>
        <code>python-basics</code>
        <code>programming-fundamentals</code>
        <code>beginner-python</code>
        <code>python-practice</code>
        <code>learning-python</code>
    </p>

</div>

</body>
</html>


