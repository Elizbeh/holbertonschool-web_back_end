function getStudentsByLocation(studentList, city){
  const filteredStudents = studentList.filter(studentList => studentList.location === city) 

  return filteredStudents
}

export default getStudentsByLocation