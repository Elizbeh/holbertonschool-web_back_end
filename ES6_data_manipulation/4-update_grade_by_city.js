// Combine
function updateStudentGradeByCity(students, city, newGrades) {
  // Filter to get students in the specified city
  const filteredStudents = students.filter(student => student.location === city);

  // Map to update grades based on newGrades array
  const updatedStudents = filteredStudents.map(student => {
    const matchingGrade = newGrades.find(grade => grade.studentId === student.id);

    return {
      id: student.id,
      firstName: student.firstName,
      location: student.location,
      grade: matchingGrade ? matchingGrade.grade : 'N/A',
    };
  });

  return updatedStudents;
}

export default updateStudentGradeByCity;
