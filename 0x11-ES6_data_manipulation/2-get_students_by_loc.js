function getStudentsByLocation(array, city) {
  return array.filter((student) => student.location === city);
}

export default getStudentsByLocation;
