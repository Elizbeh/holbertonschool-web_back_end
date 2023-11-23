function getListStudentIds(arrayOfStudents) {
  if (!Array.isArray(arrayOfStudents)) {
    return [];
  }

  // Use map function to extract ids from the array of objects
  const ids = arrayOfStudents.map((student) => student.id);

  return ids;
}

export default getListStudentIds;
