
" set hybrid numbers: current line: absolute; remaining relative
set number relativenumber 

set wildignore=build/**

" On pressing tab, insert 2 spaces
set expandtab
" show existing tab with 2 spaces width
set tabstop=2
set softtabstop=2
" when indenting with '>', use 2 spaces width
set shiftwidth=2
set bs=2

" enable clipboard
set clipboard=unnamedplus

" txx files are cpp source file
au BufNewFile,BufRead *.txx setlocal ft=cpp

" Highlight search words
set hlsearch
" Press Space to turn off highlighting and clear any message already displayed.
nnoremap <silent> <Space> :nohlsearch<Bar>:echo<CR>

" Avoid arrow keys in insert mode
inoremap <A-j> <Down>   
inoremap <A-k> <Up>
inoremap <A-h> <Left>
inoremap <A-l> <Right>

" move vim files into separate directory
set directory=~/.vim/swapfiles//
set backupdir=~/.vim/backupfiles//
set undodir=~/.vim/undofiles//
set undofile

source ~/.vimrc.plugins

" color scheme
if has('termguicolors')
  set termguicolors
endif
syntax on 
"colorscheme monokai
set background=dark
"colorscheme candid 
"colorscheme OceanicNext 
"colorscheme gruvbox
colorscheme onedark

" esearch 
let g:esearch = {}
let g:esearch.live_update = 0

" easymotion
" <Leader>f{char} to move to {char}
" map  <Leader>f <Plug>(easymotion-bd-f)
nmap f <Plug>(easymotion-overwin-f)
" s{char}{char} to move to {char}{char}
nmap s <Plug>(easymotion-overwin-f2)
" Move to line
map <Leader>l <Plug>(easymotion-bd-jk)
nmap <Leader>l <Plug>(easymotion-overwin-line)
" Move to word
" map  <Leader>w <Plug>(easymotion-bd-w)
" nmap <Leader>w <Plug>(easymotion-overwin-w)

" NERDTree
nmap <F6> :NERDTreeToggle<CR>
nmap p <S-p>

" CtrlP
nnoremap <silent> <space>f  :Files<CR>
nnoremap <silent> <space>t  :BTags<CR>
nnoremap <silent> <space>a  :Tags<CR>
nnoremap <silent> <space>m  :Buffers<CR>

" Remove trailing whitespace
autocmd FileType cc,h autocmd BufWritePre <buffer> %s/\s\+$//e

" ignore files in gitignore
" https://github.com/kien/ctrlp.vim/issues/174
" let g:ctrlp_user_command = {
"   \ 'types': {
"     \ 1: ['.git', 'cd %s && git ls-files -c --exclude-standard --recurse-submodules && git ls-files -o --exclude-standard'],
"     \ 2: ['.hg', 'hg --cwd %s locate -I .'],
"     \ },
"   \ 'fallback': 'find %s -type f'
"   \ }

" NERDCommenter
"   Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1
"   Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1
"   Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'
"   Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" gutentags
" Place a .notags file in directories with a project root that
" should be ignored
let g:gutentags_exclude_project_root = ['~/', '/usr/local']
" g:gutentags_ctags_extra_args see ~/.ctags file
" save ctag files out of source
let g:gutentags_cache_dir = expand('~/.cache/vim/ctags/')
set statusline+=%{gutentags#statusline()}

" tagbar
nmap <F8> :TagbarToggle<CR>
let g:tagbar_type_tex = {
            \ 'ctagstype' : 'latex',
            \ 'kinds'     : [
                \ 's:sections',
                \ 'g:graphics:0:0',
                \ 'l:labels',
                \ 'r:refs:1:0',
                \ 'p:pagerefs:1:0'
            \ ],
            \ 'sort'    : 0,
        \ }

" autosave
let g:auto_save = 1  " enable AutoSave on Vim startup
let g:auto_save_silent = 1  " do not display the auto-save notification

" switch between header and source file
map <F5> :call CurtineIncSw()<CR>

" required by NERDcommenter
filetype plugin on

" gitgutter
"   turn on line highlighting: toggle with GitGutterLineHighlightsToggle 
let g:gitgutter_highlight_lines = 0 
nmap <F7> :GitGutterLineHighlightsToggle<CR>

" -----------------------------------------------------------------------------
" fzf
" TODO 
"   - optimize tags: select certain category (only classes, functions,
"     prototypes, members, ...)
"   - Remove qualified names from BTags (not needed)
"   - Remove unqualified functions, prototypes and members from Tags
" https://github.com/junegunn/fzf.vim/commit/3661409e952b8532a2088226de886aea0489e281
" https://github.com/junegunn/fzf.vim/pull/620
" https://github.com/junegunn/fzf.vim/issues/293
" Customize fzf colors to match your color scheme
let g:fzf_colors =
\ { 'fg':      ['fg', 'Normal'],
  \ 'bg':      ['bg', 'Normal'],
  \ 'hl':      ['fg', 'Comment'],
  \ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
  \ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
  \ 'hl+':     ['fg', 'Statement'],
  \ 'info':    ['fg', 'PreProc'],
  \ 'prompt':  ['fg', 'Conditional'],
  \ 'pointer': ['fg', 'Exception'],
  \ 'marker':  ['fg', 'Keyword'],
  \ 'spinner': ['fg', 'Label'],
  \ 'header':  ['fg', 'Comment'] }"

let $FZF_DEFAULT_COMMAND = 'ag -g ""'

" call fzf#vim#buffer_tags('', { 'options': ['--nth', '..-2,-1', '--query', '^f$ '] })

" -----------------------------------------------------------------------------
"  coc

" coc config
let g:coc_global_extensions = [
  \ 'coc-snippets',
  \ 'coc-pairs',
  \ 'coc-tsserver',
  \ 'coc-eslint', 
  \ 'coc-prettier', 
  \ 'coc-json', 
  \ ]
" from readme
" if hidden is not set, TextEdit might fail.
set hidden " Some servers have issues with backup files, see #649 set nobackup set nowritebackup " Better display for messages set cmdheight=2 " You will have bad experience for diagnostic messages when it's default 4000.
set updatetime=300

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

"" Use `[g` and `]g` to navigate diagnostics
"nmap <silent> [g <Plug>(coc-diagnostic-prev)
"nmap <silent> ]g <Plug>(coc-diagnostic-next)

"" Remap keys for gotos
"nmap <silent> gd <Plug>(coc-definition)
"nmap <silent> gy <Plug>(coc-type-definition)
"nmap <silent> gi <Plug>(coc-implementation)
"nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <F2> <Plug>(coc-rename)

"" Remap for format selected region
"xmap <leader>f  <Plug>(coc-format-selected)
"nmap <leader>f  <Plug>(coc-format-selected)

"augroup mygroup
  "autocmd!
  "" Setup formatexpr specified filetype(s).
  "autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  "" Update signature help on jump placeholder
  "autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
"augroup end

"" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
"xmap <leader>a  <Plug>(coc-codeaction-selected)
"nmap <leader>a  <Plug>(coc-codeaction-selected)

"" Remap for do codeAction of current line
"nmap <leader>ac  <Plug>(coc-codeaction)
"" Fix autofix problem of current line
"nmap <leader>qf  <Plug>(coc-fix-current)

"" Create mappings for function text object, requires document symbols feature of languageserver.
"xmap if <Plug>(coc-funcobj-i)
"xmap af <Plug>(coc-funcobj-a)
"omap if <Plug>(coc-funcobj-i)
"omap af <Plug>(coc-funcobj-a)

"" Use <C-d> for select selections ranges, needs server support, like: coc-tsserver, coc-python
"nmap <silent> <C-d> <Plug>(coc-range-select)
"xmap <silent> <C-d> <Plug>(coc-range-select)

"" Use `:Format` to format current buffer
"command! -nargs=0 Format :call CocAction('format')

"" Use `:Fold` to fold current buffer
"command! -nargs=? Fold :call     CocAction('fold', <f-args>)

"" use `:OR` for organize import of current buffer
"command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

"" Add status line support, for integration with other plugin, checkout `:h coc-status`
"set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

"" Using CocList
"" Show all diagnostics
"nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
"" Manage extensions
"nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
"" Show commands
"nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
"" Find symbol of current document
"nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
"" Search workspace symbols
"nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
"" Do default action for next item.
"nnoremap <silent> <space>j  :<C-u>CocNext<CR>
"" Do default action for previous item.
"nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
"" Resume latest coc list
"nnoremap <silent> <space>p  :<C-u>CocListResume<CR>


