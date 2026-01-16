var minimumArea = function (grid) {
  let m = grid.length;
  let n = grid[0].length;

  let top = m,
    bottom = -1;
  let left = n,
    right = -1;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        top = Math.min(top, i);
        bottom = Math.max(bottom, i);
        left = Math.min(left, j);
        right = Math.max(right, j);
      }
    }
  }

  let height = bottom - top + 1;
  let width = right - left + 1;

  return height * width;
};
