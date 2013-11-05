" part of script is copied form https://github.com/yodiaditya/vim-pydjango/blob/master/.vimrc
" added script for maping keys , virtual env and removed unwanted packges

set nocompatible " be iMproved
filetype off                   " required!

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
set t_Co=256
" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'
Bundle 'jmcantrell/vim-virtualenv'

" Files manager

Bundle 'majutsushi/tagbar'
Bundle 'L9'
Bundle 'FuzzyFinder'

"Bundle 'vim-scripts/mru.vim'
"Bundle 'fholgado/minibufexpl.vim'

Bundle 'scrooloose/nerdtree'
Bundle 'jistr/vim-nerdtree-tabs'
Bundle 'sjl/gundo.vim'

" Color scheme
Bundle 'cschlueter/vim-mustang'
Bundle 'godlygeek/csapprox'

" Utilities
Bundle "tsaleh/vim-matchit"
Bundle 'Raimondi/delimitMate'

" Syntax Commenter
Bundle 'vim-scripts/tComment'

" HTML Development 
Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}

" Universal Syntax Checker + Completion
"Bundle 'UltiSnips'
Bundle 'scrooloose/syntastic'
"Bundle "Shougo/neocomplcache"

" Python "
Bundle 'kevinw/pyflakes-vim'
Bundle 'vim-scripts/pep8'
Bundle 'davidhalter/jedi-vim'
Bundle 'klen/python-mode'
Bundle "vim-scripts/indentpython.vim"
"Bundle "jmcomets/vim-pony"


" Versioning System
Bundle 'tpope/vim-fugitive'


if filereadable('/home/juned/Code/pinry/.vimrc-virtualenv')
      source /home/juned/Code/pinry/.vimrc-virtualenv
endif
let g:virtualenv_directory = '/home/juned/Code/pinry/'

map <c-\> :vsplit<cr>
map <leader>t (g:fuf_keyOpenVsplit)
"filetype plugin indent on     " required!
"map <S-Up> <C-w>+<cr>
"map <S-Down> <C-w>-<cr> 
map <S-Right> :5winc ><cr>
map <S-Down> :5winc <<cr>
map <S-Up> :5winc +<cr>
map <S-Down> :5winc -<cr>



map <c-Right> <c-w><Right>
map <c-Left> <c-w><Left>
map <c-Up> <c-w><Up>
map <c-down> <c-w><Down>

set noswapfile
let g:virtualenv_directory = "/home/Code/pinry/"
let g:pymode_rope = 0

let g:pymode_doc = 1
let g:pymode_doc_key = 'K'



let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all


let g:pymode_folding =0
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Sets how many lines of history VIM has to remember
set history=1000

" Ignore some file
set wildignore=*.swp,*.bak,*.pyc,*.class

" Set to auto read when a file is changed from the outside
set autowrite

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set tabstop=4
set softtabstop=4
set shiftwidth=4
set textwidth=80
set smarttab
set expandtab

set lbr
set tw=500

set ai "Auto indent
set si "Smart indet
set wrap "Wrap lines


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => VIM user interface
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set so=7            " Set 7 lines to the curors - when moving vertical..
set ruler           "Always show current position
set hid             "Change buffer - without saving
set nohidden
set mouse=a

" Set backspace config
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

set nolazyredraw "Don't redraw while executing macros 
set magic "Set magic on, for regular expressions

set showmatch "Show matching bracets when text indicator is over them

" No sound on errors
set noerrorbells
set novisualbell
set tm=500

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax enable "Enable syntax hl

set shell=/bin/bash

set guioptions-=T
set background=dark
colorscheme mustang
set nonu
set gfn=Liberation\ Mono\ 10 

set encoding=utf8
try
    lang en_US
catch
endtry

if has("gui_running")
  " GUI is running or is about to start.
  " Maximize gvim window.
  set lines=43
  set co=87
endif

autocmd FileType python highlight OverLength ctermbg=darkred ctermfg=white guibg=#FFD9D9
autocmd FileType python match OverLength /\%81v.\+/


set nowrap " no line wrapping;
set guioptions+=b " add a horizontal scrollbar to the bottom


"--- search options ------------
set incsearch " show 'best match so far' as you type
set hlsearch " hilight the items found by the search
set ignorecase " ignores case of letters on searches
set smartcase " Override the 'ignorecase' option if the search pattern contains upper case characters


" Search and error color highlights
hi Search guifg=#ffffff guibg=#0000ff gui=none ctermfg=white ctermbg=darkblue
hi IncSearch guifg=#ffffff guibg=#8888ff gui=none ctermfg=white
highlight SpellBad guifg=#ffffff guibg=#8888ff gui=none ctermfg=black ctermbg=darkred

set showcmd

""" PYTHON STYLE """"
let python_highlight_all=1 " Enable all plugin's highlighting.
let python_slow_sync=1 " For fast machines.
let python_print_as_function=1 " Color 'print' function.



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Pep8 using F6
" You can change with this :
let g:pep8_map='<F6>'



""""""""""""""""""""""""""""""""""""""""""""""""
" Auto close preview menu autocomplete after choose
" http://stackoverflow.com/questions/3105307/how-do-you-automatically-remove-the-preview-window-after-autocompletion-in-vim
"
" If you prefer the Omni-Completion tip window to close when a selection is
" made, these lines close it on movement in insert mode or when leaving
" insert mode
autocmd CursorMovedI * if pumvisible() == 0|pclose|endif
autocmd InsertLeave * if pumvisible() == 0|pclose|endif




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Pyflakes configuration
if has("gui_running")
    highlight SpellBad term=underline gui=undercurl guisp=Orange
endif

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Configure neocomplcache autocomplete
" http://www.vim.org/scripts/script.php?script_id=2620


highlight Pmenu gui=bold

if has("gui_running")
    highlight SpellBad term=underline gui=undercurl guisp=Orange
endif


" Set autocomplete form
set completeopt=menuone,longest,preview

"--- python formatting help ---
autocmd BufRead *.py set smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class

" Enable omni completion.
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown,ctp set omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType php,ctp set omnifunc=phpcomplete#CompletePHP
autocmd FileType vim set omnifunc=syntaxcomplete#Complete



"""""""""""""""""""""""""""""""""""
"if has("autocmd")
"    au FileType qf
"                \ if &buftype == "quickfix" |
""                \ setlocal statusline=%2*%-3.3n%0* |
""                \ setlocal statusline+=\ \[Compiler\ Messages\] |
 ""               \ setlocal statusline+=%=%2*\ %<%P |
 ""               \ endif

""    fun! FixMiniBufExplorerTitle()
 ""       if "-MiniBufExplorer-" == bufname("%")
""            setlocal statusline=%2*%-3.3n%0*
""            setlocal statusline=%2*%-3.3n%0*
""            setlocal statusline+=\[Buffers\]
""            setlocal statusline+=%=%2*\ %<%P
""        endif
""    endfun
""
""    au BufWinEnter *
""                \ let oldwinnr=winnr() |
""                \ windo call FixMiniBufExplorerTitle() |
""                \ exec oldwinnr . " wincmd w"
""endif
  

" FuzzFinder Shorcuts.
map <leader>f :FufFileWithCurrentBufferDir<CR>
map <leader>m :FufFileWithFullCwd<CR>
map <leader>t :FufBuffer<CR>

map <c-f> :NERDTreeToggle<CR>

" TagBar Configuration
let g:tagbar_usearrows=1
let g:tagbar_width=30
let g:tagbar_singleclick=1

" Use leader + l to open Tagbar in Right side
nnoremap <leader>l :TagbarToggle<CR>
