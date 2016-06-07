" let filename = expand('%:p')

"Fix the stupid messages
set shortmess=filnxtToO

"Initial skip count
let g:skip=0

"Increments global skip
function! IncSkip()
  let g:skip = g:skip + 1
endfunction

"Decrement global skip
function! DecSkip()
  let g:skip = g:skip - 1
endfunction

"Returns a tmp file name for a file in a commit
function! FileInCommit(file, commit)
  let prefix = substitute(system("git rev-parse --show-prefix"), '\n', '', '')
  let tmpfile = "/tmp/file_" . a:commit
  call system("git show " . a:commit . ":" . l:prefix . a:file . " > " . l:tmpfile)
  return l:tmpfile
endfunction

"Return a commit for a file, given a skip
function! CommitWithSkip(file, skip)
  return substitute(system("git log --format=\"%h\" --skip=" . a:skip . " -n 1 " . a:file), '\n', '', '')
endfunction

"Opens two buffers, one for current skip and one for previous
function! OpenCurrentSkipBuffers(file)
  execute 'edit ' . FileInCommit(a:file, CommitWithSkip(a:file, g:skip + 1))
  execute 'vert diffsplit ' . FileInCommit(a:file, CommitWithSkip(a:file, g:skip))
endfunction

"Clear the screen
function! ClearScreen()
  execute ':bd'
  execute ':bd'
endfunction

"Open previous pair of diffs
function! PreviousDiff()
  call ClearScreen()
  call IncSkip()
  call OpenCurrentSkipBuffers(g:filename)
endfunction

"Open next pair of diffs
function! NextDiff()
  call ClearScreen()
  call DecSkip()
  call OpenCurrentSkipBuffers(g:filename)
endfunction

"Keymaps
map q :qa<Return>
map <Right> :call PreviousDiff()<Return>
map <Left> :call NextDiff()<Return>

call OpenCurrentSkipBuffers(g:filename)
