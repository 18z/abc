let g:zdict_query_key = '<leader>z'
execute 'nnoremap <silent> '. g:zdict_query_key .' :call zdict#query()<CR>'


function! s:get_word () " {{{
    let l:mode = mode()

    if l:mode == 'n'
        return expand('<cWORD>')
    elseif l:mode == 'v' || l:mode == 'V' || l:mode == ""
        if line("'<") != line("'>")
            return ''
        endif
        return getline('.')[(col("'<") - 1):(col("'>") - 1)]
    elseif l:mode == 'i'
        let l:linetext = getline('.')
        let l:right = col('.') - 1
        let l:left = l:right
        while l:left > 1
            if l:linetext[(l:left - 1)] ==# ' '
                let l:left = l:left + 1
                break
            endif
            let l:left = l:left - 1
            echom l:linetext[(l:left - 1):(l:right - 1)]
        endwhile
        return l:linetext[(l:left - 1):(l:right - 1)]
    endif

    return expand('<cWORD>')
endfunction " }}}


function! zdict#query () " {{{
    let l:word = s:get_word()
    echo l:word
endfunction " }}}
