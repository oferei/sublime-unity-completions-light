import sublime, sublime_plugin

class CsharpCompletions(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		if not view.match_selector(locations[0], 'source.cs -string -comment -constant'):
			return []

		compl_default = [view.extract_completions(prefix)]
		compl_default = [(item + "\tDefault", item) for sublist in compl_default
			for item in sublist if len(item) > 3]       # flatten
		compl_default = list(set(compl_default))        # make unique

		return (compl_default)
