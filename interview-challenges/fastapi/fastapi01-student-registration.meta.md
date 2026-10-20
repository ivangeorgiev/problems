# FastAPI Student Registration

University is made of **Departments**. **Departments** offer **Courses**. **Professors** belong to a **Department** and teach multiple **Course Sections**. **Students** belong to a department and enroll in many **Course Sections**. **Course Section** has many **Student Enrollments**.

## Task 1: Create conceptual ER diagram.

```mermaid
erDiagram
    department
    professor
    student
    course
    course_section
    student_course_section_enrollment

    professor }o--|| department : "belongs to"
    student }o--|| department : "belongs to"
    department ||--o{ course : "offers"
    course ||--o{ course_section : "split in"
    professor ||--o{ course_section : "teaches"
    student ||--o{ student_course_section_enrollment : enrolls
    student_course_section_enrollment }o--|| course_section : enrolls
```

