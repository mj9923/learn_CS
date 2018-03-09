require './Egoing'

module K8805
  module_function
  def a()
    return 'B'
  end
end

puts(Egoing.a())
puts(K8805.a())
