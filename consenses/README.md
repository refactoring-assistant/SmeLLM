# Human-LLM-Cross-Validation
This repo introduces a human-LLM-cross-validation method for the code smell dataset.

Our dataset encompasses 23 code smells derived from Martin Fowler's canonical refactoring references. Initially designed with binary encoding—where each file pair was labeled with a single, isolated code smell—the dataset has been enhanced through a novel validation methodology. By conducting LLM-based detection experiments and human-expert annotations, we observed significant co-occurrence patterns among certain code smells. Leveraging LLM consensus analysis, we systematically identified and reintegrated these co-existing code smells back into the expected labels, thereby reducing human labeling errors and providing a more robust representation of code smell manifestations for evaluation purposes.

The Python script conducts consensus analysis on the FP-positive, FP-negative metrics from the test results of experimented LLMs.


## Development
To install these modules, users can simply run:

```pip install -r requirements.txt ```

Or if they want to use it within a virtual environment (recommended):

```python3 -m venv venv ```

``` source venv/bin/activate ```   On macOS/Linux, or

``` venv\Scripts\activate ```  On Windows

## Dependency
There is prerequisite to run file `set_manipulation.py`.
However, file `set_manipulation.py` is imported to run file `consensus.py`.


## Run consensus.py
To run consenses analysis on excel result sheets obtained from SmeLLM, 
configure excel sheets as constants: 

* In file 'consensus.py': RUNNER_CONFIG as a key-value pair, where the key is the name of the model, and the value is the path to the excel sheet of that model.
* The RUNNER_CONFIG as a whole indicates which group of baseline models that the consensus is drawn from.
 

## Terminology
Define,
* **Collective False Positive (CFP)**: All LLMs under experiments detect the underlying code smell, but the code smell is not labeled as expected in the test sheet.

* **Collective False Negative (CFN)**: All LLMs under experiments fail to detect the underlying code smell, but the code is labeled as expected in the test sheet.

* **Collective True Positive (CTP)**: All LLMs under experiments detects the underlying code smell, and the code smell is labaled as expected in the test sheet.

* **Collective True Negative (CTN)**: All LLMs under experiments don't detect the underlying code smell, and the code smell is not labeled as expected in the test sheet.

Under the hood,
* **Collective False Positive (CFP)**: Even though the underlying code smell was not expected during the human curation process, all LLMs under experiment still detect the code smell in one file.

* **Collective False Negative (CFN)**: Even though the underlying code smell was expected during the human curation process, all LLMs under experiment fail to detect the code smell in one file. 

* **Collective True Positive (CTP)**: The underlying code smell was expected during the human curation process, and all LLMs under experiment detect the code smell in one file.

* **Collective True Negative (CTN)**: The underlying code smell was not expected during the human curation process, and all LLMs under experiment don't detect the code smell in one file.


# Mathematical Expressions for Collective Metrics
- **E** = Expected (ground truth) set of code smells
- **Ē** (or **E̅**) = Complement of E = U − E (code smells NOT in ground truth)
- **A₁, A₂, ..., Aₙ** = Actual detected sets from n LLMs/tools
- **Āᵢ** (or **A̅ᵢ**) = Complement of Aᵢ = U − Aᵢ (code smells NOT detected by tool i)
- **U** = Universal set of all possible code smells (ALL_CODE_SMELLS)
- **⋂** = Intersection operator
- **−** = Set difference operator
- **n** = Number of LLMs/tools being compared

---

## 1. Collective True Positive (TP)

### Individual TP for tool i:
```
TPᵢ = E ∩ Aᵢ
```

### Collective TP (intersection of all individual TPs):
```
Collective_TP = ⋂ᵢ₌₁ⁿ TPᵢ = ⋂ᵢ₌₁ⁿ (E ∩ Aᵢ)
```

### Simplified form:
```
Collective_TP = E ∩ (⋂ᵢ₌₁ⁿ Aᵢ)
```

**Interpretation:** Code smells that exist in ground truth AND were detected by ALL tools

---

## 2. Collective False Positive (FP)

### Individual FP for tool i:
```
FPᵢ = Aᵢ − E = Aᵢ ∩ Ē
```

### Collective FP (intersection of all individual FPs):
```
Collective_FP = ⋂ᵢ₌₁ⁿ FPᵢ = ⋂ᵢ₌₁ⁿ (Aᵢ − E) = ⋂ᵢ₌₁ⁿ (Aᵢ ∩ Ē)
```

**Interpretation:** Code smells that don't exist in ground truth BUT were incorrectly detected by ALL tools

---

## 3. Collective True Negative (TN)

### Individual TN for tool i:
```
TNᵢ = U − E − Aᵢ = Ē ∩ Āᵢ
```

### Collective TN (intersection of all individual TNs):
```
Collective_TN = ⋂ᵢ₌₁ⁿ TNᵢ = ⋂ᵢ₌₁ⁿ (U − E − Aᵢ) = ⋂ᵢ₌₁ⁿ (Ē ∩ Āᵢ)
```

### Simplified form:
```
Collective_TN = Ē ∩ (⋂ᵢ₌₁ⁿ Āᵢ)
```

**Interpretation:** Code smells that don't exist in ground truth AND were NOT detected by ANY tool

---

## 4. Collective False Negative (FN)

### Individual FN for tool i:
```
FNᵢ = E − Aᵢ = E ∩ Āᵢ
```

### Collective FN (intersection of all individual FNs):
```
Collective_FN = ⋂ᵢ₌₁ⁿ FNᵢ = ⋂ᵢ₌₁ⁿ (E − Aᵢ) = ⋂ᵢ₌₁ⁿ (E ∩ Āᵢ)
```

### Simplified form:
```
Collective_FN = E ∩ (⋂ᵢ₌₁ⁿ Āᵢ)
```

**Interpretation:** Code smells that exist in ground truth BUT were missed by ALL tools

---

## Summary Table

| Metric | Individual Metric | Alternative Form | Collective Metric | Interpretation |
|--------|-------------------|------------------|-------------------|----------------|
| **TP** | `E ∩ Aᵢ` | — | `⋂ᵢ₌₁ⁿ (E ∩ Aᵢ)` | ALL tools got it right |
| **FP** | `Aᵢ − E` | `Aᵢ ∩ Ē` | `⋂ᵢ₌₁ⁿ (Aᵢ ∩ Ē)` | ALL tools got it wrong (same way) |
| **TN** | `U − E − Aᵢ` | `Ē ∩ Āᵢ` | `⋂ᵢ₌₁ⁿ (Ē ∩ Āᵢ)` | ALL tools correctly ignored it |
| **FN** | `E − Aᵢ` | `E ∩ Āᵢ` | `⋂ᵢ₌₁ⁿ (E ∩ Āᵢ)` | ALL tools missed it |

---

## Summary

The collective metrics measure **complete agreement** among all tools:
- **Collective TP**: Smells that everyone correctly identified
- **Collective FP**: Smells that everyone incorrectly identified
- **Collective TN**: Smells that everyone correctly ignored
- **Collective FN**: Smells that everyone missed

These represent the **intersection of individual metric sets**, showing where all LLMs/tools are in unanimous agreement.









    
