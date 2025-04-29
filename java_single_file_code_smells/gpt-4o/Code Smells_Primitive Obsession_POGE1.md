**Code Review: POGE1.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - The `printPatientDetails` method in the `PatientGood` class (~90~ to ~98~) and the `printMedicalHistory` method in the `MedicalHistory` class (~140~ to ~152~) are handling multiple responsibilities.
- Found in line no. - [90, 140]
- Possible treatments - Extract Method
- Possible solution - 

```java
class PatientGood {
    // Other fields and methods

    public void printPatientDetails() {
        printName();
        printAddress();
        printInsuranceNumber();
        printMedicalData();
    }

    private void printName() {
        System.out.println("Patient Name: " + patientName.getFirstName() + " " + patientName.getLastName());
    }

    private void printAddress() {
        System.out.println("Patient Address: " + patientAddress.getAddress());
    }

    private void printInsuranceNumber() {
        System.out.println("Insurance Number: " + insuranceNumber);
    }

    private void printMedicalData() {
        System.out.println("Blood Group: " + medicalBioData.getBloodGroup());
        System.out.println("Height: " + medicalBioData.getHeight());
        System.out.println("Weight: " + medicalBioData.getWeight());
        System.out.println("Age: " + medicalBioData.getAge());
    }
}

class MedicalHistory {
    // Other fields and methods

    public void printMedicalHistory() {
        printPreviousMedications();
        printAllergies();
        printDiseaseHistory();
    }

    private void printPreviousMedications() {
        System.out.println("Previous Medication: ");
        for (MedicationHistory medication : previousMedication) {
            System.out.println(medication.getMedication() + " - " + medication.getDuration());
        }
    }

    private void printAllergies() {
        System.out.println("Allergies: ");
        for (String allergy : allergies) {
            System.out.println(allergy);
        }
    }

    private void printDiseaseHistory() {
        System.out.println("Disease History: ");
        for (String disease : diseaseHistory) {
            System.out.println(disease);
        }
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Usage of strings to represent domain concepts such as `bloodGroup`, `height`, `weight`, and `age`, which could be encapsulated into specific types.
- Found in line no. - [22, 23, 24, 25]
- Possible treatments - Replace Data Value with Object 
- Possible solution - 

```java
class BloodGroup {
    private final String bloodGroup;

    public BloodGroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }
}

class Height {
    private final String height;

    public Height(String height) {
        this.height = height;
    }

    public String getHeight() {
        return height;
    }
}

class Weight {
    private final String weight;

    public Weight(String weight) {
        this.weight = weight;
    }

    public String getWeight() {
        return weight;
    }
}

class Age {
    private final String age;

    public Age(String age) {
        this.age = age;
    }

    public String getAge() {
        return age;
    }
}

class MedicalBioDataGood {
    private final BloodGroup bloodGroup;
    private final Height height;
    private final Weight weight;
    private final Age age;

    public MedicalBioDataGood(BloodGroup bloodGroup, Height height, Weight weight, Age age) {
        this.bloodGroup = bloodGroup;
        this.height = height;
        this.weight = weight;
        this.age = age;
    }

    public String getBloodGroup() {
        return bloodGroup.getBloodGroup();
    }

    public String getHeight() {
        return height.getHeight();
    }

    public String getWeight() {
        return weight.getWeight();
    }

    public String getAge() {
        return age.getAge();
    }
}
```

**No additional code smells detected in the remaining classes.**