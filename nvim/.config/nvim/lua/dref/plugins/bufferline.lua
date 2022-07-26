local ok, bufferline = pcall(require, "bufferline")
if not ok then
	return
end

bufferline.setup {
	options = {
		diagnostics = "nvim_lsp",
		diagnostics_update_in_insert = false,
	}
}
