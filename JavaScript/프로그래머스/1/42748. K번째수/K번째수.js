function solution(array, commands) {
  let answer = []

  commands.map(command => {
    tmp1 = array.slice(command[0] - 1, command[1])
    // console.log(tmp1)
    sort(tmp1)
    // console.log(tmp1)
    answer.push(tmp1[command[2] - 1])
  }
  )

  // console.log(answer)
  return answer
}

function sort(arr) {
  for (let i in arr)
    for (let j = 0; j < arr.length - i - 1; j++)
      if (arr[j] > arr[j + 1])
        swap(arr, j, j + 1)
}

function swap(arr, sour, dest) {
  let tmp1 = arr[sour]
  arr[sour] = arr[dest]
  arr[dest] = tmp1
}

// console.assert(JSON.stringify(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) === JSON.stringify([5, 6, 3]), "틀렸습니다.")
// console.assert(JSON.stringify(solution([10, 2], [[1, 2, 1]])) === JSON.stringify([2]), "틀렸습니다.")
