function getStudentIdsSum(studentList) {
  const studentIdSum = studentList.reduce((accumulator,
    studentList) => accumulator + studentList.id, 0);

  return studentIdSum;
}

export default getStudentIdsSum;
