
class HealthRecord {
    private String patientIdentifier;
    private String bloodGroup;
    private String height;
    private String weight;
    private String age;
    private String [] patientName;
    private String [] patientAddress;
    private String insuranceNumber;
    private String [] previousMedication;
    private String [] durationOfMedication;
    private String [] allergies;
    private String [] diseaseHistory;

  public HealthRecord(String patientIdentifier, String [] patientName, String [] patientAddress,
                         String insuranceNumber) {
    this.patientIdentifier = patientIdentifier;
    this.patientName = patientName;
    this.patientAddress = patientAddress;
    this.insuranceNumber = insuranceNumber;
    this.bloodGroup = "N/A";
    this.height = "N/A";
    this.weight = "N/A";
    this.age = "N/A";
    this.previousMedication = new String[10];
    this.durationOfMedication = new String[10];
    this.allergies = new String[10];
    this.diseaseHistory = new String[10];
  }

    public void updatePatientMedicalData(String [] medicalBiodata) {
        this.bloodGroup = medicalBiodata[0];
        this.height = medicalBiodata[1];
        this.weight = medicalBiodata[2];
        this.age = medicalBiodata[3];
    }

    public void addPreviousMedication(String patientIdentifier, String medication, String duration) {
    if(!verifyPatient(patientIdentifier)) {
      System.out.println("Patient not found");
      return;
    }
        for (int i = 0; i < previousMedication.length; i++) {
            if (previousMedication[i] == null) {
                previousMedication[i] = medication;
                durationOfMedication[i] = duration;
                break;
            }
        }
    }

    public void addAllergy(String patientIdentifier, String allergy) {
      if(!verifyPatient(patientIdentifier)) {
        System.out.println("Patient not found");
        return;
      }
        for (int i = 0; i < allergies.length; i++) {
            if (allergies[i] == null) {
                allergies[i] = allergy;
                break;
            }
        }
    }

    public void addDiseaseHistory(String patientIdentifier, String disease) {
      if(!verifyPatient(patientIdentifier)) {
        System.out.println("Patient not found");
        return;
      }
        for (int i = 0; i < diseaseHistory.length; i++) {
            if (diseaseHistory[i] == null) {
                diseaseHistory[i] = disease;
                break;
            }
        }
    }

    public void printMedicalRecord() {
        System.out.println("Patient Name: " + patientName[0] + " " + patientName[1]);
        System.out.println("Patient Address: " + patientAddress[0] + " " + patientAddress[1] + " " + patientAddress[2] + " " + patientAddress[3] + " " + patientAddress[4] + " " + patientAddress[5]);
        System.out.println("Insurance Number: " + insuranceNumber);
        System.out.println("Blood Group: " + bloodGroup + "\nHeight: " + height + "\nWeight: " + weight + "\nAge: " + age);
        printPrevMedication();
        printAllergies();
        printDiseaseHistory();
    }

    private boolean verifyPatient(String patientIdentifier) {
        return this.patientIdentifier.equals(patientIdentifier);
    }

    private void printPrevMedication() {
      System.out.println("Previous Medication: ");
        for (int i = 0; i < previousMedication.length; i++) {
            if (previousMedication[i] != null) {
                System.out.println(previousMedication[i] + " - " + durationOfMedication[i]);
            }
        }
    }

    private void printAllergies() {
      System.out.println("Allergies: ");
        for (int i = 0; i < allergies.length; i++) {
            if (allergies[i] != null) {
                System.out.println(allergies[i]);
            }
        }
    }

    private void printDiseaseHistory() {
      System.out.println("Disease History: ");
        for (int i = 0; i < diseaseHistory.length; i++) {
            if (diseaseHistory[i] != null) {
                System.out.println(diseaseHistory[i]);
            }
        }
    }
}
public class source52 {
  public static void main(String[] args) {
    String [] patientName = {"John", "Doe"};
    String [] patientAddress = {"123", "Main", "Street", "City", "State", "Country"};
    String [] medicalBiodata = {"O+", "6", "70", "30"};
    HealthRecord healthRecord = new HealthRecord("123", patientName, patientAddress, "1234");
    healthRecord.updatePatientMedicalData(medicalBiodata);
    healthRecord.addPreviousMedication("123", "Paracetamol", "3 times a day");
    healthRecord.addAllergy("123", "Peanuts");
    healthRecord.addDiseaseHistory("123", "Fever");
    healthRecord.printMedicalRecord();
  }
}
