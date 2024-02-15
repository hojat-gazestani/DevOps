" Django file configuration
autocmd FileType python setlocal ft=python.django

" Enable syntax highlighting for Django templates
au BufNewFile,BufRead *.html set filetype=html.django
au BufNewFile,BufRead *.jinja set filetype=html.django

" Set indentation settings for Python
autocmd FileType python setlocal expandtab tabstop=4 shiftwidth=4

" Set indentation settings for Django templates
autocmd FileType html.django setlocal expandtab tabstop=2 shiftwidth=2

" Enable line numbers
set number

" Enable syntax highlighting
syntax enable

" Enable auto-indentation
set autoindent
set smartindent

" Highlight current line
set cursorline

" Enable folding
set foldmethod=indent
set foldlevel=1

" Show matching brackets/parentheses
set showmatch

" Enable code folding with markers
au FileType python set foldmarker=#region,#endregion
au FileType html.django set foldmarker={% block,% endblock %}

" Show invisible characters (such as tabs and trailing spaces)
set list
set listchars=tab:▸\ ,trail:·

" Enable smooth scrolling
set scrolloff=5

" Enable incremental search highlighting
set incsearch

" Enable persistent undo
set undofile

" Disable swap files
set noswapfile

" Enable mouse support in all modes
" set mouse=a

" Customize colorscheme (replace 'desert' with your preferred colorscheme)
syntax enable

" General settings
set ruler

" Enable line wrapping
set wrap

call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'

" Configure gruvbox colorscheme
set termguicolors
set background=dark
colorscheme gruvbox

" YAML file configuration
au BufNewFile,BufRead *.yml set filetype=yaml

" Set indentation settings for YAML
autocmd FileType yaml setlocal expandtab tabstop=2 shiftwidth=2

" Enable syntax highlighting for YAML
autocmd FileType yaml syntax enable
autocmd FileType yaml syntax match Comment "#.*$"

" Enable auto-indentation for YAML
autocmd FileType yaml setlocal autoindent

" Highlight YAML keys
autocmd FileType yaml highlight yamlKey ctermfg=Yellow gui=bold

" Highlight YAML values
autocmd FileType yaml highlight yamlValue ctermfg=Cyan gui=none

" Highlight YAML sequences
autocmd FileType yaml highlight yamlSequence ctermfg=Green gui=none

" Highlight YAML anchors and aliases
autocmd FileType yaml highlight yamlAnchor ctermfg=Magenta gui=none

" Customize colors for syntax highlighting
" You can modify these colors to your preference
highlight yamlKey ctermfg=Yellow gui=bold
highlight yamlValue ctermfg=Cyan gui=none
highlight yamlSequence ctermfg=Green gui=none
highlight yamlAnchor ctermfg=Magenta gui=none

" Enable Go-specific settings
autocmd FileType go setlocal expandtab tabstop=4 shiftwidth=4

" Enable Go linting with 'golint' command
let g:syntastic_go_checkers = ['golint']

" Enable Go formatting with 'gofmt' command
let g:go_fmt_command = "gofmt"

" Enable completion with 'vim-go' plugin
Plug 'fatih/vim-go'
