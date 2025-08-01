import java.util.ArrayList;
import java.util.List;
class Name {
    private final String firstName;
    private final String lastName;

    public Name(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }
}

class MedicalBioData {
    private final String bloodGroup;
    private final String height;
    private final String weight;
    private final String age;

    public MedicalBioData(String bloodGroup, String height, String weight, String age) {
        this.bloodGroup = bloodGroup;
        this.height = height;
        this.weight = weight;
        this.age = age;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public String getHeight() {
        return height;
    }

    public String getWeight() {
        return weight;
    }

    public String getAge() {
        return age;
    }
}

class Address {
    private final String street;
    private final String city;
    private final String state;
    private final String country;

    public Address(String street, String city, String state, String country) {
        this.street = street;
        this.city = city;
        this.state = state;
        this.country = country;
    }
    public String getAddress() {
        return street + ", " + city + ", " + state + ", " + country;
    }
}
class Patient {
  private String patientIdentifier;
  private Name patientName;
  private Address patientAddress;
  private String insuranceNumber;
  private MedicalBioData medicalBioData;

  public Patient(String patientIdentifier, Name patientName, Address patientAddress, String insuranceNumber) {
    this.patientIdentifier = patientIdentifier;
    this.patientName = patientName;
    this.patientAddress = patientAddress;
    this.insuranceNumber = insuranceNumber;
    this.medicalBioData = null;
  }

  public void updatePatientMedicalData(MedicalBioData medicalBioData) {
    this.medicalBioData = medicalBioData;
  }

  public boolean verifyPatient(String patientIdentifier) {
    return this.patientIdentifier.equals(patientIdentifier);
  }

  public void printPatientDetails() {
    System.out.println("Patient Name: " + patientName.getFirstName() + " " + patientName.getLastName());
    System.out.println("Patient Address: " + patientAddress.getAddress());
    System.out.println("Insurance Number: " + insuranceNumber);
    System.out.println("Blood Group: " + medicalBioData.getBloodGroup());
    System.out.println("Height: " + medicalBioData.getHeight());
    System.out.println("Weight: " + medicalBioData.getWeight());
    System.out.println("Age: " + medicalBioData.getAge());
  }
}

class MedicationHistory  {
  private String medication;
  private String duration;

  public MedicationHistory(String medication, String duration) {
    this.medication = medication;
    this.duration = duration;
  }

  public String getMedication() {
    return medication;
  }

  public String getDuration() {
    return duration;
  }
}
class MedicalHistory {
    private List<MedicationHistory> previousMedication;
    private List<String> allergies;
    private List<String> diseaseHistory;

    public MedicalHistory() {
        this.previousMedication = new ArrayList<>();
        this.allergies = new ArrayList<>();
        this.diseaseHistory = new ArrayList<>();
    }

    public void addPreviousMedication(MedicationHistory newMedication) {
        previousMedication.add(newMedication);
    }

    public void addAllergy(String allergy) {
        allergies.add(allergy);
    }
    public void addDiseaseHistory(String disease) {
        diseaseHistory.add(disease);
    }

    public void printMedicalHistory() {
        System.out.println("Previous Medication: ");
        for (MedicationHistory medication : previousMedication) {
            System.out.println(medication.getMedication() + " - " + medication.getDuration());
        }
        System.out.println("Allergies: ");
        for (String allergy : allergies) {
            System.out.println(allergy);
        }
        System.out.println("Disease History: ");
        for (String disease : diseaseHistory) {
            System.out.println(disease);
        }
    }
}
class HealthRecord {
  private Patient patient;
  private MedicalHistory medicalHistory;

  public HealthRecord(Patient patient) {
    this.patient = patient;
    this.medicalHistory = new MedicalHistory();
  }

  public void addPreviousMedication(String patientIdentifier, MedicationHistory medication) {
    if(!patient.verifyPatient(patientIdentifier)) {
      System.out.println("Patient not found");
      return;
    }
    medicalHistory.addPreviousMedication(medication);
  }

  public void addAllergy(String patientIdentifier, String allergy) {
    if(!patient.verifyPatient(patientIdentifier)) {
      System.out.println("Patient not found");
      return;
    }
    medicalHistory.addAllergy(allergy);
  }

  public void addDiseaseHistory(String patientIdentifier, String disease) {
    if(!patient.verifyPatient(patientIdentifier)) {
      System.out.println("Patient not found");
      return;
    }
    medicalHistory.addDiseaseHistory(disease);
  }

  public void printMedicalRecord() {
    patient.printPatientDetails();
    medicalHistory.printMedicalHistory();
  }
}
public class source54 {
  public static void main(String[] args) {
    Name patientName = new Name("John", "Doe");
    Address patientAddress = new Address("123 Main St", "City", "State", "Country");
    MedicalBioData medicalBioData = new MedicalBioData("O+", "6", "70", "30");
    Patient patient = new Patient("123", patientName, patientAddress, "1234");
    patient.updatePatientMedicalData(medicalBioData);
    HealthRecord healthRecord = new HealthRecord(patient);
    MedicationHistory medication1 = new MedicationHistory("Paracetamol", "3 times a day");
    healthRecord.addPreviousMedication("123", medication1);
    healthRecord.addAllergy("123", "Peanuts");
    healthRecord.addDiseaseHistory("123", "Fever");
    healthRecord.printMedicalRecord();
  }
}
